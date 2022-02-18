from django.urls import path

from . import views

urlpatterns = (
    path('', views.TaskListView.as_view(), name='task.list'),
    path('create', views.TaskCreateView.as_view(), name='task.create'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='task.detail'),
    path('<int:task_id>/update', views.update_task, name='task.update'),
)
