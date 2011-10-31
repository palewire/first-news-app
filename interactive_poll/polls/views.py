from django.db.models import Sum
from polls.models import Project, Vote
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    projects = Project.objects.all().order_by('-pub_date')[:5]
    return render(request, 'index.html', {
        'projects': projects
    })


def detail(request, poll_id):
    p = Project.objects.get(pk=poll_id)
    total = p.vote_set.aggregate(Sum('choice'))
    return render(request, 'detail.html', {
        'project': p,
        'total': total['choice__sum'],
        'request': request,
    })


@csrf_exempt
def vote(request, poll_id):
    p = get_object_or_404(Project, pk=poll_id)
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


