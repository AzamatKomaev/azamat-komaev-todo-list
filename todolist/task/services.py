from typing import Optional

from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from .models import Task


class TaskService:
    task: Task

    def __init__(self, task: Task):
        self.task = task

    def is_user_owner(self, user: User) -> bool:
        return self.task.user == user

    def update(self, is_done: bool):
        self.task.is_done = is_done
        self.task.save()
        return self.task

    @staticmethod
    def create(data: dict) -> Task:
        task = Task.objects.create(**data)
        return task

    @staticmethod
    def get_queryset(sort_type: str, user_username: Optional[int]) -> QuerySet[Task]:
        tasks: QuerySet[Task] = Task.objects.none()
        print(sort_type, user_username)

        if sort_type == "created_at":
            tasks = Task.objects.all()

        elif sort_type == "filter_by_user":
            tasks = Task.objects.filter(user__username=user_username)

        elif sort_type == "updated_at":
            tasks = Task.objects.order_by('-updated_at')

        elif sort_type == "only_done":
            tasks = Task.objects.filter(is_done=True)

        elif sort_type == "only_in_progress":
            tasks = Task.objects.filter(is_done=False)

        return tasks

