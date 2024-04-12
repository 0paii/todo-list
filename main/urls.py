from django.urls import path
from main.views import create_task, delete_task, edit_task, change_complete, SearchResultsView

app_name = 'task'

urlpatterns = [
    path('task/', create_task, name='create_task'),
    path('task/delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('task/edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('task/change_complete/<int:task_id>/', change_complete, name='change_complete'),
    path('search/', SearchResultsView.as_view(), name='search_results')
]
