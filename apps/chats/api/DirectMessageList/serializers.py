from rest_framework import serializers
from apps.chats.models import DirectMessage


class DirectMessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = (
            "id",
            "user",
            "chat",
            "text",
            "created_at",
        )


__all__ = ("DirectMessageListSerializer",)
