from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.clients.api.ClientsList.serializers import ClientSerializer
from apps.clients.models import Client


class ClientsListAPIView(ListAPIView):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Client.objects.all()


__all__ = ("ClientsListAPIView",)
