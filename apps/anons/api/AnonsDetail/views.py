from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.anons.api.AnonsDetail.serializers import AnonsDetailSerializer
from apps.anons.models import Anons


class AnonsDetailView(RetrieveAPIView):
    serializer_class = AnonsDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Anons.objects.all()


__all__ = ("AnonsDetailView",)
