from django.db import models

class ProjectPriority(models.TextChoices):
    LOW = 'low', 'Low'
    MEDIUM = 'medium', 'Medium'
    HIGH = 'high', 'High'
    VERY_HIGH = 'very high', 'Very High'
    CRITICAL = 'critical', 'Critical'


    class ProjectPriority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'
        VERY_HIGH = 'very high', 'Very High'
        CRITICAL = 'critical', 'Critical'

        @classmethod
        def get_choices(cls):
            """Вернуть пары (value, label), как в стандартном .choices"""
            return [(item.value, item.label) for item in cls]

        @classmethod
        def values(cls):
            """Вернуть только значения"""
            return [item.value for item in cls]

        @classmethod
        def labels(cls):
            """Вернуть только подписи (читаемые названия)"""
            return [item.label for item in cls]
