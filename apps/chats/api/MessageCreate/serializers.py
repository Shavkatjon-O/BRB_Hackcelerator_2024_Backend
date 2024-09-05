from rest_framework import serializers
from apps.chats.models import Message


class MessageCreateSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=1000)
    chat_id = serializers.IntegerField()

    class Meta:
        model = Message
        fields = (
            "text",
            "chat_id",
        )


__all__ = ("MessageCreateSerializer",)
