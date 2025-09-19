# from django.contrib import admin
#
# # Register your models here.
# from django.contrib import admin
# from .models import Task, Tag
# from .models import ProjectPriority, ProjectStatus
#
#
#
# # Register your models here.
# def make_action(field, value, description):
#     """
#     Генерирует action для изменения поля field на value
#     """
#     def action(modeladmin, request, queryset):
#         queryset.update(**{field: value})
#     action.short_description = description
#     action.__name__ = f"{field}_{value}".replace(" ", "_")
#     return action
#
#
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     search_fields = ['title']
#     list_display = ['title', 'project', 'status', 'priority', 'created', 'due_date']
#     list_filter = ['status', 'priority', 'project', 'created', 'due_date']
#
#     # Actions для приоритетов
#     actions = [
#         make_action('priority', value, f"Установка приоритета {label}")
#         for value, label in ProjectPriority.choices
#     ]
#
#     # Actions для статусов
#     actions += [
#         make_action('status', value, f"Установка статуса {label}")
#         for value, label in ProjectStatus.choices
#     ]
#
#     @admin.action(description="Закрыть выбранные задачи")
#     def close_tasks(self, request, queryset):
#         queryset.update(status=ProjectStatus.CLOSED)
#
#     actions.append('close_tasks')
#
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     verbose_name = 'Tag'
#     verbose_name_plural = 'Tags'
#     list_display = ('name',)
#
#
#
