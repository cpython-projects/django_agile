from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .models import Project, ProjectFile
from .serializers import ProjectSerializer, ProjectDetailSerializer, ProjectFileSerializer

def get_project(project_id):
    try:
        return Project.objects.get(pk=project_id)

    except Project.DoesNotExist:
        raise NotFound(detail=f'Проект (id={project_id}) не найден')

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


# ======================= Projects ==================================
@api_view(['GET', 'POST'])
def project_list_create(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    serializer = ProjectDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'GET':
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'
        serializer = ProjectDetailSerializer(project, data=request.data, partial=partial)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# =========================== Project Files ======================================
@api_view(['GET', 'POST'])
def projectfile_list_create(request):
    if request.method == 'GET':
        files = ProjectFile.objects.all()
        serializer = ProjectFileSerializer(files, many=True)
        return Response(serializer.data)

    serializer = ProjectFileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def projectfile_detail(request, pk):
    file_obj = get_object_or_404(ProjectFile, pk=pk)

    if request.method == 'GET':
        serializer = ProjectFileSerializer(file_obj)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'
        serializer = ProjectFileSerializer(file_obj, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        file_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
