from django.contrib.auth.models import User
from django.db import models
from apps.projects.models import Project
from apps.tasks.choices import ProjectStatus,ProjectPriority
from apps.tasks.utils import calculate_end_of_month

from apps.tasks.models import Tag


class Task(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=ProjectStatus.choices, default=ProjectStatus.NEW)
    priority = models.CharField(max_length=15, choices=ProjectPriority.choices, default=ProjectPriority.MEDIUM)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(default=calculate_end_of_month)
    assigned = models.ForeignKey(User, null=True, blank=True, related_name='assigned_tasks', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ('-due_date', 'assigned',)
        unique_together = (('project', 'title'),)

    def __str__(self):
        return self.title
