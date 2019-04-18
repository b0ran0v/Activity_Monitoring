from django.shortcuts import render, get_object_or_404
from .models import Project, Task


def project_list(request):
    projects = Project.objects.order_by('date_created')
    return render(request, 'Project_Management/project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.all().filter(project=project)
    return render(request, 'Project_Management/project_detail.html', {'project': project, 'tasks': tasks})

