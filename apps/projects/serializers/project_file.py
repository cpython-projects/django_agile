from rest_framework.relations import StringRelatedField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import ProjectFile


class ProjectFileSerializer(ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['id', 'name', 'file', 'created_at']


