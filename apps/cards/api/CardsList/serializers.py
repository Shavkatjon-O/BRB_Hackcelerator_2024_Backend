from rest_framework import serializers
from apps.cards.models import Card


class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            "id",
            "client",
            "card_number",
            "card_type",
            "currency",
            "balance",
            "status",
            "expiration_date",
            "created_by",
            "approved_by",
        )


__all__ = ("CardListSerializer",)
