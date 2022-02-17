from django.views.generic import ListView

from .models import Task


class TaskListView(ListView):
    queryset = Task.objects.all()
    context_object_name = 'tasks'
    template_name = 'task/task_list.jinja'
