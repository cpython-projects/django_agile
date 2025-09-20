from django.urls import path
from . import views

urlpatterns = [
    # Tasks
    path('tasks/', views.task_list_create, name='task-list-create'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),

    # Tags
    path('tags/', views.tag_list_create, name='tag-list-create'),
    path('tags/<int:pk>/', views.tag_detail, name='tag-detail'),
]
