from typing import Optional

from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import JsonResponse
from django.db.models.query import QuerySet

from .forms import TaskForm
from .models import Task
from .services import TaskService


class TaskListView(ListView):
    context_object_name = 'tasks'
    template_name = 'task/task_list.jinja'

    def get_queryset(self) -> QuerySet[Optional[Task]]:
        sort_type = self.request.GET.get('sort_type', 'created_at')
        user_username = self.request.GET.get('user_username', None)

        try:
            tasks = TaskService.get_queryset(sort_type, user_username)
            return tasks
        except tasks.DoesNotExist:
            return Task.objects.none()


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.jinja'


class TaskView(View):
    http_method_names = ('patch', 'post', 'get')
    form = TaskForm()
    template_post_name = 'task/task_create.jinja'

    def get(self, request):
        return render(request, self.template_post_name, {'form': self.form})

    def post(self, request):
        self.form = TaskForm(request.POST)
        if self.form.is_valid():
            task = TaskService.create(data={**self.form.cleaned_data, **{'user': request.user}})
            return redirect('task.detail', pk=task.id)

        return render(request, self.template_post_name, {'form': self.form})

    def patch(self, request, task_id: int):
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

@login_required
def create_task(request):
    template_name = "task/task_create.jinja"

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = TaskService.create(data={**form.cleaned_data, **{'user': request.user}})
            return redirect('task.detail', pk=task.id)

    else:
        form = TaskForm()

    return render(request, template_name, {'form': form})



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
