from django.urls import path
from .views import ProjectsListAPIView, ProjectsDetailAPIView

urlpatterns = [
    path('projects/', ProjectsListAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectsDetailAPIView.as_view(), name='project-detail'),
]
