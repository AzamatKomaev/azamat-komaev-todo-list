from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tasks'
        ordering = ('-created_at',)
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
