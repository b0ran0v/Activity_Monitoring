# Generated by Django 2.2 on 2019-04-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_Activity_Monitoring', '0005_auto_20190418_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name=['django.contrib.auth.backends.ModelBackend', 'field_permissions.backends.InstancePermissionBackend']),
        ),
    ]
