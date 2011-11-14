from django.shortcuts import render
from states.models import ActivityLevel, Week


def index(request):
    latest_week = Week.objects.all().order_by("-end_date")[0]
    object_list = ActivityLevel.objects.filter(week=latest_week)
    context = {
        'object_list': object_list,
        'week': latest_week,
    }
    return render(request, 'index.html', context)
