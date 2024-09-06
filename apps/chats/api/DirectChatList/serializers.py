from rest_framework import serializers
from apps.chats.models import DirectChat

from apps.chats.api.UserList.serializers import UserListSerializer


class DirectChatListSerializer(serializers.ModelSerializer):
    user1 = UserListSerializer()
    user2 = UserListSerializer()

    class Meta:
        model = DirectChat
        fields = (
            "id",
            "user1",
            "user2",
        )


__all__ = ("DirectChatListSerializer",)
