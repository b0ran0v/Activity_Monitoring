from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.utils import timezone
from .models import Project, Task, User
from .forms import ProjectForm, TaskForm
from django.contrib.auth.views import auth_login, auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def main_page(request):
    is_manager = False
    if request.user.groups.filter(name__in=['Manager']).exists():
        is_manager = True
    return render(request, 'Project_Management/base.html', {'is_manager': is_manager})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.get_user()
            user1 = User.objects.get(username=username)
            auth_login(request, username)
            if user1.groups.filter(name__in=['Manager']).exists():
                return redirect('/project_list')
            elif user1.groups.filter(name__in=['Developer']).exists():
                return redirect('/task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'Project_Management/login.html', {'form': form})


def logout_view(request):
    if request.user:
        auth_logout(request)
    return redirect('/accounts/login')


@login_required(login_url='/accounts/login')
def project_list(request):
    if request.user.groups.filter(name__in=['Manager']).exists():
        projects = Project.objects.filter(project_manager=request.user).order_by('date_created')
        return render(request, 'Project_Management/project_list.html', {'projects': projects})
    return render(request, 'Project_Management/base.html')


@login_required(login_url='/accounts/login')
def project_detail(request, pk):
    if request.user.groups.filter(name__in=['Manager']).exists():
        project = get_object_or_404(Project, pk=pk)
        tasks = Task.objects.all().filter(project=project)
        tasks_finished = Task.objects.all().filter(project=project, is_finished=True)
        progress = (float(tasks_finished.count())/tasks.count())*100
        return render(request, 'Project_Management/project_detail.html',
                      {'project': project, 'tasks': tasks, 'progress': progress})
    return render(request, 'Project_Management/base.html')


def task_list(request):
    tasks = Task.objects.all().filter(developer=request.user).order_by('date_assigned')
    return render(request, 'Activity_Management/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    is_manager = False
    if request.user.groups.filter(name__in=['Manager']).exists():
        is_manager = True
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'Activity_Management/task_detail.html',
                  {'task': task, 'is_manager': is_manager})


def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.date_created = timezone.now()
            project.project_manager = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'Project_Management/project_edit.html', {'form': form})


def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.date_assigned = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'Activity_Management/task_edit.html', {'form': form})


def task_finish(request, pk):
    is_manager = False
    if request.user.groups.filter(name__in=['Manager']).exists():
        is_manager = True
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=pk)
        if task.is_finished is True:
            task.is_finished = False
        else:
            task.is_finished = True
        task.save()
        return render(request, 'Activity_Management/task_detail.html',
                      {'task': task, 'is_manager': is_manager})
    return redirect('task_detail', pk=pk)
