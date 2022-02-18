from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse

from .forms import TaskForm
from .models import Task
from .services import TaskService


class TaskListView(ListView):
    queryset = Task.objects.all()
    context_object_name = 'tasks'
    template_name = 'task/task_list.jinja'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.jinja'


class TaskCreateView(FormView):
    form_class = TaskForm
    template_name = 'task/task_create.jinja'

    @login_required
    def dispatch(self, request, *args, **kwargs):
        super(TaskCreateView, self).dispatch(request, *args, **kwargs)


@login_required
def update_task(request, task_id: int):
    if request.method == "PATCH":
        task = get_object_or_404(Task, pk=task_id)
        task_service = TaskService(task)

        if not task_service.is_user_owner(request.user):
            return JsonResponse({}, status=403)

        updated_task = task_service.update(is_done=True)

        if not updated_task:
            return JsonResponse({}, status=403)

        return JsonResponse({
            "status": 200
        })
