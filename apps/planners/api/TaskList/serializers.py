from rest_framework import serializers
from apps.planners.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "status",
            "due_date",
            "completed_date",
            "created_by",
        )


__all__ = ("TaskSerializer",)
