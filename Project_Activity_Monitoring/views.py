from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.order_by('date_created')
    return render(request, 'Project_Management/project_list.html', {'projects': projects})

