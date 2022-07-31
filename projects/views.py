from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
import projects

from projects.models import Project

from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects
    return render(request, 'projects/index.html', {'projects':projects})


def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project_detail})



