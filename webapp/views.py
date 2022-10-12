from django.db.models import Q
from django.shortcuts import render

from webapp.models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'webapp/index.html', {'projects': projects})


def about(request):

    return render(request, 'webapp/about.html')


def search(request):
    text = request.GET.get('search')
    if text:
        projects = Project.objects.filter(
            Q(title__contains=text)|Q(description__contains=text)
        )
    else:
        projects = Project.objects.none()
    return render(request, 'webapp/search_results.html', {'projects': projects})
