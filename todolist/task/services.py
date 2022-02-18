from django.contrib.auth.models import User

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
