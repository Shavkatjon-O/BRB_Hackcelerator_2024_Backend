from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.clients.api.ClientsDetail.serializers import ClientDetailSerializer
from apps.clients.models import Client


class ClientsDetailAPIView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ("ClientsDetailAPIView",)
