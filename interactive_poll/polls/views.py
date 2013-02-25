from django.db.models import Sum
from polls.models import Poll
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def index(request):
    poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'index.html', {
        'poll_list': poll_list
    })

def detail(request, poll_id):
     p = Poll.objects.get(pk=poll_id)
     total = p.vote_set.aggregate(sum=Sum('choice'))
     return render(request, 'detail.html', {
         'poll': p,
         'total': total['sum'] or 0,
         'request': request,
     })

@csrf_exempt
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    data = request.POST.get("data", None)
    if not data:
        return HttpResponse(status=405)
    if data == "-1":
        value = -1
    else:
        value = 1
    v = p.vote_set.create(choice=value)
    v.save()
    return HttpResponse(status=200)
