from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404
from .serializers import (AllProjectsSerializer, CreateProjectSerializer, ProjectDetailSerializer,
                           AllProjectFileSerializer, CreateProjectFileSerializer)
from rest_framework.exceptions import NotFound
from .models import Project, ProjectFile


"""
Создать сериализатор ProjectDetailSerializer
Написать классовое отображение ProjectDetailAPIView (методы get, put, delete)
Реализовать эндпоинт:
    GET /api/v1/projects/<id>/ — получить проект
    PUT /api/v1/projects/<id>/ — обновить проект (поддержка частичного обновления)
    DELETE /api/v1/projects/<id>/ — удалить проект
Проверить работу запросов"""
class ProjectDetailAPIView(APIView):
    def get(self, request, pk):

        project = get_project(pk)
        serializer = ProjectDetailSerializer(project)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        project = get_project(pk)
        serializer = ProjectDetailSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        project = get_project(pk)
        serializer = ProjectDetailSerializer(project, data=request.data, partial=True)  # частичное
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = get_project(pk)
        project.delete()

        return Response({"message": f"Deleted project (id={pk}) success"}, status=status.HTTP_204_NO_CONTENT)

class ProjectsListAPIView(APIView):
    """
    GET: список проектов с фильтрацией по date_from и date_to
    POST: создать новый проект с валидацией description >= 30 символов
    """
    def get(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')

        projects = Project.objects.all()
        if date_from:
            projects = projects.filter(created_at__date__gte=parse_date(date_from))
        if date_to:
            projects = projects.filter(created_at__date__lte=parse_date(date_to))

        serializer = AllProjectsSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectsDetailAPIView(APIView):
    """
    GET: получить проект по id
    PUT/PATCH: обновить проект
    DELETE: удалить проект
    """
    def get_object(self, pk):
        return get_object_or_404(Project, pk=pk)

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def get_project(project_id):
    try:
        return Project.objects.get(pk=project_id)

    except Project.DoesNotExist:
        raise NotFound(detail=f'Проект (id={project_id}) не найден')

class ProjectFileListAPIView(APIView):
    """
    GET: список файлов (с фильтром по имени проекта ?project=NAME)
    POST: загрузка нового файла
    """

    def get(self, request):
        projects_name = request.query_params.get('project')
        queryset = ProjectFile.objects.all()
        if projects_name:
            queryset = queryset.filter(projects__name__icontains=projects_name)

        serializer = AllProjectFileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateProjectFileSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(CreateProjectFileSerializer(data).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

