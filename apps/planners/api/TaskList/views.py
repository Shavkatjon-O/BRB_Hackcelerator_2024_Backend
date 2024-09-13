from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.planners.api.TaskList.serializers import TaskSerializer
from apps.planners.models import Task


class TaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()


__all__ = ("TaskListAPIView",)
