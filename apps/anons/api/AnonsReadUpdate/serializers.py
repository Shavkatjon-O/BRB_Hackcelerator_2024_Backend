from rest_framework import serializers
from apps.anons.models import Anons


class AnonsReadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anons
        fields = ("id",)


__all__ = ("AnonsReadUpdateSerializer",)
