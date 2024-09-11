from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.clients.api.ClientsCreate.serializers import ClientCreateSerializer
from apps.clients.models import Client


class ClientsCreateAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ("ClientsCreateAPIView",)
