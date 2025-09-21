from django.urls import path
from .views import task_list_create, task_detail, TagListAPIView, tag_detail

urlpatterns = [
    # Tasks
    path('tasks/', task_list_create, name='task-list-create'),
    path('tasks/<int:pk>/', task_detail, name='task-detail'),

    # Tags
    path('tasks/tags/', TagListAPIView.as_view(), name='tag-list-create'),
    path('tasks/tags/<int:pk>/', tag_detail, name='tag-detail'),
]
