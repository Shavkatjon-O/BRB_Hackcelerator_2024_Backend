from rest_framework import serializers
from apps.chats.models import Chat


class GroupChatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            "id",
            "users",
            "title",
            "image",
        )


__all__ = ("GroupChatDetailSerializer",)
