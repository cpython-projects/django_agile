from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from ..models import Task
from . import TagSerializer


class TaskSerializer(ModelSerializer):
    project = StringRelatedField()
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'project', 'tags', 'created_at', 'due_date', 'updated_at', 'deleted_at', 'assigned'
        ]



