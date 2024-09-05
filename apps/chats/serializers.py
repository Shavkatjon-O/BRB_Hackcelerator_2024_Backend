from rest_framework import serializers
from apps.chats.models import Message, Chat
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "image",
        )


class ChatSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = (
            "id",
            "title",
            "image",
            "is_group",
            "users",
        )


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    chat = ChatSerializer()

    class Meta:
        model = Message
        fields = (
            "id",
            "user",
            "chat",
            "text",
            "created_at",
        )
