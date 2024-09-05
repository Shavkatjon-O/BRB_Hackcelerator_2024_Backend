from rest_framework import serializers
from apps.chats.models import Chat


class DirectChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            "id",
            "users",
        )


__all__ = ("DirectChatListSerializer",)
