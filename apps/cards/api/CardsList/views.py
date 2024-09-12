from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cards.api.CardsList.serializers import CardListSerializer
from apps.cards.models import Card


class CardsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CardListSerializer
    queryset = Card.objects.all()


__all__ = ("CardsListView",)
