# Generated by Django 5.0.4 on 2024-04-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_delete_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end_task_date',
            field=models.DateTimeField(default=None),
        ),
    ]
