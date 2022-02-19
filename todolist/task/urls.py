from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    path('', views.TaskListView.as_view(), name='task.list'),
    path('create', login_required(views.TaskView.as_view()), name='task.create'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='task.detail'),
    path('<int:task_id>/update', login_required(views.TaskView.as_view()), name='task.update'),
)
