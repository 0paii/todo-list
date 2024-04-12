from django.contrib import admin
from main.models import Task


# Register your models here.

@admin.register(Task)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description', 'complete')
    ordering = ('name', 'description')
    search_fields = ('name', 'description', "end_date_field")
