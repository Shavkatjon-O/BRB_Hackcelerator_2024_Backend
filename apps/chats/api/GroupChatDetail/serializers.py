from rest_framework import serializers
from apps.chats.models import GroupChat


class GroupChatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = (
            "id",
            "users",
            "image",
            "title",
        )


__all__ = ("GroupChatDetailSerializer",)
