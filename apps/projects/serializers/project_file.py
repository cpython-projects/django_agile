from rest_framework.relations import StringRelatedField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import ProjectFile, Project
from ..utils.file_utils import check_extension, check_file_size

class ProjectFileSerializer(ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['id', 'name', 'file', 'created_at']


#AllProjectFilesSerializer — список файлов
class AllProjectFileSerializer(ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = "__all__"


#CreateProjectFileSerializer — загрузка нового файла (валидация имени и расширения, проверка размера ≤ 2MB)
class CreateProjectFileSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all(), required=False)
    class Meta:
        model = ProjectFile
        fields = ['name','file','projects']

    def validate_file(self, value):
        check_extension(value.name)
        check_file_size(value)
        return value

    def create(self, validated_data):
        """
        Создаём ProjectFile и автоматически сохраняем файл.
        """
        projects = validated_data.pop('projects', [])
        file = ProjectFile.objects.create(**validated_data)
        if projects:
            file.projects.set(projects)
        return file