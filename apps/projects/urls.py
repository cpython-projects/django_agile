from django.urls import path
from . import views


urlpatterns = [

    # Projects
    path('projects/', views.project_list_create, name='project-list-create'),
    path('projects/<int:pk>/', views.project_detail, name='project-detail'),

    # Project Files
    path('files/', views.projectfile_list_create, name='projectfile-list-create'),
    path('files/<int:pk>/', views.projectfile_detail, name='projectfile-detail'),
    path("projects/files/", views.ProjectFileListAPIView.as_view(), name="project-files"),
]
    # GET /api/v1/projects/files/ — вернёт список всех файлов.
    # GET /api/v1/projects/files/?project=Demo — вернёт только файлы проекта Demo.
    # POST /api/v1/projects/files/ — загрузит файл (проверка имени и расширения, размер ≤ 2 MB, привязка к проекту).