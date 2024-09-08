from rest_framework import serializers

from apps.chats.models import DirectChat
from apps.chats.api.UserList.serializers import UserListSerializer


class DirectChatDetailSerializer(serializers.ModelSerializer):
    partner = serializers.SerializerMethodField()

    class Meta:
        model = DirectChat
        fields = ("id", "partner")

    def get_partner(self, obj):
        if obj.user1 == self.context["request"].user:
            return UserListSerializer(obj.user2).data
        return UserListSerializer(obj.user1).data


__all__ = ("DirectChatDetailSerializer",)
