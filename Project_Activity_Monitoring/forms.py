from django import forms
from .models import Project, Task
from django.contrib.admin import widgets


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description', 'deadline')


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'project', 'developer', 'deadline')
