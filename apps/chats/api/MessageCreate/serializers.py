from rest_framework import serializers
from apps.chats.models import Message


class MessageCreateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)
    chat_id = serializers.IntegerField()


__all__ = ("MessageCreateSerializer",)
