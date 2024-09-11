from django.urls import path

from apps.planners.api.TaskList.views import TaskListAPIView

urlpatterns = [
    path("", TaskListAPIView.as_view(), name="task-list"),
]
