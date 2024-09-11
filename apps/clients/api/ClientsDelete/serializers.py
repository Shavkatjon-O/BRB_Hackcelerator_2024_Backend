from rest_framework import serializers
from apps.clients.models import Client


class ClientDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id",)


__all__ = ("ClientDeleteSerializer",)
