from rest_framework import serializers
from apps.chats.models import Message


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            "id",
            "user",
            "chat",
            "text",
            "created_at",
        )


__all__ = ("MessageListSerializer",)
