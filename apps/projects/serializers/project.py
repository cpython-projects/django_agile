from rest_framework.relations import StringRelatedField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class ProjectDetailSerializer(ModelSerializer):
    tasks = StringRelatedField(many=True, read_only=True)
    files_count = serializers.IntegerField(source='count_files', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'tasks', 'files_count']
