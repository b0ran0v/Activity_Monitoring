from django.conf import settings
from django.db import models
from django.utils import timezone
from field_permissions.models import FieldPermissionModelMixin
from django.contrib.auth.models import AbstractUser


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    project_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                        blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Task(FieldPermissionModelMixin, models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_finished = models.BooleanField(settings.AUTHENTICATION_BACKENDS, default=False)
    date_assigned = models.DateField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        permissions = (('can_change_task_status', 'Can change task status'),)