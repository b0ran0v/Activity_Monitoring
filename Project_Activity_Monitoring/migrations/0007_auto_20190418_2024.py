# Generated by Django 2.2 on 2019-04-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_Activity_Monitoring', '0006_auto_20190418_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deadline'),
        ),
    ]
