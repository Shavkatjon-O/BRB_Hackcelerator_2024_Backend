from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.applications.api.ApplicationsList.serializers import (
    ApplicationsListSerializer,
)
from apps.applications.models import Application


class ApplicationsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationsListSerializer
    queryset = Application.objects.all()


__all__ = ("ApplicationsListAPIView",)
