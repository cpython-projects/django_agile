from django.db import models


class ProjectStatus(models.TextChoices):
    NEW = 'NEW', 'New'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    COMPLETED = 'COMPLETED', 'Completed'
    CLOSED = 'CLOSED', 'Closed'
    PENDING = 'PENDING', 'Pending'
    BLOCKED = 'BLOCKED', 'Blocked'

    @classmethod
    def values(cls):
        return [s.value for s in cls]