from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.anons.api.AnonsList.serializers import AnonsListSerializer
from apps.anons.models import Anons


class AnonsListView(ListAPIView):
    serializer_class = AnonsListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Anons.objects.all()


__all__ = ("AnonsListView",)
