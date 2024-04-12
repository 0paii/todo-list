from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView
from main.forms import CreateTaskForm
from main.models import Task
from main.base.base import TitleMixin
import json


# Create your views here.


class IndexView(TitleMixin, TemplateView):
    template_name = 'index.html'
    title = 'Task'

    def get_context_data(self, **kwargs):
        form = CreateTaskForm()
        context = super(IndexView, self).get_context_data()
        context.update({"Tasks": Task.objects.all(), 'form': form})
        return context


class SearchResultsView(TitleMixin, ListView):
    title = 'Search'
    model = Task
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Task.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list


def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('index'))
    else:
        form = CreateTaskForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse_lazy('index'))


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CreateTaskForm(instance=task)
    context = {'task_id': task_id, "form": form, 'title': f"Changing task {task.name}"}
    return render(request, 'edit_task.html', context)


def change_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.complete = json.loads(request.POST.get('status', None))
    task.save()
    return JsonResponse({'success': True})
