from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.chats.models import Chat, Message

User = get_user_model()


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


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Message
        fields = (
            "id",
            "chat",
            "user",
            "text",
            "created_at",
        )


class ChatSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = (
            "id",
            "title",
            "users",
            "messages",
            "created_at",
        )
