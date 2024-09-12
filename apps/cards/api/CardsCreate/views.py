from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cards.api.CardsCreate.serializers import CardCreateSerializer
from apps.cards.models import Card


class CardsCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CardCreateSerializer
    queryset = Card.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


__all__ = ("CardsCreateView",)
