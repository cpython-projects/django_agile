from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from ..models import Project


class AllProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at']


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description']

    def validate_description(self, value):
        if not value or len(value.strip()) < 30:
            raise serializers.ValidationError("Description must be at least 30 characters.")
        return value


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class ProjectDetailSerializer(serializers.ModelSerializer):
    tasks = StringRelatedField(many=True, read_only=True)
    files_count = serializers.IntegerField(source='count_files', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'tasks', 'files_count']
