from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.clients.api.ClientsDelete.serializers import ClientDeleteSerializer
from apps.clients.models import Client


class ClientsDeleteAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDeleteSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ("ClientsDeleteAPIView",)
