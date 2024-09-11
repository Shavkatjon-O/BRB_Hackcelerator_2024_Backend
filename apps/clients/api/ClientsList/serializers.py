from rest_framework import serializers
from apps.clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "full_name",
            "gender",
            "email",
            "birth_date",
            "phone_number",
            "city",
            "postal_code",
            "country",
            "address",
            "identification_number",
            "credit_score",
            "image",
            "is_active",
        )


__all__ = ("ClientSerializer",)
