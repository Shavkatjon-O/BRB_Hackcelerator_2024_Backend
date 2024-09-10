from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from apps.anons.api.AnonsList.serializers import AnonsListSerializer
from apps.anons.models import Anons


class AnonsListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000


class AnonsListView(ListAPIView):
    serializer_class = AnonsListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Anons.objects.all()
    pagination_class = AnonsListPagination


__all__ = ("AnonsListView",)
