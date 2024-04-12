from django.db import models


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    end_task_date = models.DateTimeField(default=None)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name
