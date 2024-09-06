from rest_framework import serializers
from apps.chats.models import DirectMessage

from apps.chats.api.UserList.serializers import UserListSerializer
from apps.chats.api.DirectChatList.serializers import DirectChatListSerializer


class DirectMessageListSerializer(serializers.ModelSerializer):
    user = UserListSerializer()
    chat = DirectChatListSerializer()

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
