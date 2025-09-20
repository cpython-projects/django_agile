from django.contrib import admin
from .models import Task, Tag, ProjectPriority, ProjectStatus


def make_action(field, value, description):
    """
    Генерирует action для изменения поля field на value
    """
    def action(modeladmin, request, queryset):
        queryset.update(**{field: value})
    action.short_description = description
    action.__name__ = f"{field}_{value}".replace(" ", "_")
    return action


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'project', 'status', 'priority', 'updated_at', 'due_date', 'deadline']
    list_filter = ['status', 'priority', 'project', 'updated_at', 'due_date', 'deadline']

    actions = []

    actions += [
        make_action('priority', value, f"Установить приоритет: {label}")
        for value, label in ProjectPriority.choices
    ]

    actions += [
        make_action('status', value, f"Установить статус: {label}")
        for value, label in ProjectStatus.choices
    ]

    @admin.action(description="Закрыть выбранные задачи")
    def close_tasks(self, request, queryset):
        queryset.update(status=ProjectStatus.CLOSED)

    actions.append(close_tasks)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
