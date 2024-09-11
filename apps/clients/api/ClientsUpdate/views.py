from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.clients.api.ClientsUpdate.serializers import ClientUpdateSerializer
from apps.clients.models import Client


class ClientsUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ("ClientsUpdateAPIView",)
