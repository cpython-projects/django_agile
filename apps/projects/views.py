# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# from .models import Project, Task, Tag
# from .serializers import (
#     ProjectSerializer,
#     ProjectDetailSerializer,
#     TaskSerializer,
#     TagSerializer
# )
#
#
# def home(request):
#     return HttpResponse("<h1>Welcome to Practic_2 API</h1><p>Use /api/v1/ for API endpoints.</p>")
#
#
# # ======================= Projects ==================================
# @api_view(['GET', 'POST'])
# def project_list_create(request):
#     if request.method == 'GET':
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)
#
#     serializer = ProjectDetailSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def project_detail(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#
#     if request.method == 'GET':
#         serializer = ProjectDetailSerializer(project)
#         return Response(serializer.data)
#
#     elif request.method in ['PUT', 'PATCH']:
#         partial = request.method == 'PATCH'
#         serializer = ProjectDetailSerializer(project, data=request.data, partial=partial)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         project.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#
# # =========================== Task ======================================
# @api_view(['GET', 'POST'])
# def task_list_create(request):
#     if request.method == 'GET':
#         project_name = request.query_params.get('project')
#         if not project_name:
#             all_tasks = Task.objects.all()
#         else:
#             all_tasks = Task.objects.filter(project=project_name)
#
#         if not all_tasks.exists():  # Correct way to check queryset emptiness
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = TaskSerializer(all_tasks, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)  # Properly indented
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def task_detail(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#     elif request.method in ['PUT', 'PATCH']:
#         partial = request.method == 'PATCH'
#         serializer = TaskSerializer(task, data=request.data, partial=partial)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#
# # ====================== Tags ================================
#
# @api_view(['GET', 'POST'])
# def tag_list_create(request):
#     if request.method == 'GET':
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
#     serializer = TagSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def tag_detail(request, pk):
#     tag = get_object_or_404(Tag, pk=pk)
#     if request.method == 'GET':
#         serializer = TagSerializer(tag)
#         return Response(serializer.data)
#     elif request.method in ['PUT', 'PATCH']:
#         partial = request.method == 'PATCH'
#         serializer = TagSerializer(tag, data=request.data, partial=partial)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         tag.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#
# from django.shortcuts import render
#
# # Create your views here.
