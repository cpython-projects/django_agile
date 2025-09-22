from django.urls import path
from . import views

urlpatterns = [

    # Projects
    path('', views.project_list_create, name='project-list-create'),
    path('<int:pk>', views.ProjectDetailAPIView.as_view(), name='project-detail-apiview'),

    # Project Files
    path('files/', views.projectfile_list_create, name='projectfile-list-create'),
    path('files/<int:pk>/', views.projectfile_detail, name='projectfile-detail'),
]
