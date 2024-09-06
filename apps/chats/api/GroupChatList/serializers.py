from rest_framework import serializers
from apps.chats.models import GroupChat


class GroupChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = (
            "id",
            "users",
            "image",
            "title",
        )


__all__ = ("GroupChatListSerializer",)
