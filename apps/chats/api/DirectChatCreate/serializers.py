from rest_framework import serializers
from apps.chats.models import Chat


class DirectChatCreateSerializer(serializers.ModelSerializer):
    users = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Chat
        fields = (
            "id",
            "users",
        )

    def validate_users(self, value):
        if len(value) != 1:
            raise serializers.ValidationError(
                "You must specify exactly one other user for a private chat."
            )
        return value


__all__ = ("DirectChatCreateSerializer",)
