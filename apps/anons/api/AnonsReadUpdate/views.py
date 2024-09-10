from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.anons.models import Anons
from apps.anons.api.AnonsReadUpdate.serializers import AnonsReadUpdateSerializer


class AnonsReadUpdate(UpdateAPIView):
    serializer_class = AnonsReadUpdateSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Anons.objects.all()

    def perform_update(self, serializer):
        anons = Anons.objects.get(pk=self.kwargs["pk"])

        if not anons.read_by.filter(id=self.request.user.id).exists():
            anons.read_by.add(self.request.user)
            anons.save()


__all__ = ("AnonsReadUpdate",)
