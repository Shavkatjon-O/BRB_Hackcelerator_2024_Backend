from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.messages.models import Chat, Message

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


class ChatSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    last_message = serializers.StringRelatedField()  # Adjust if needed

    class Meta:
        model = Chat
        fields = (
            "id",
            "participants",
            "last_message",
        )


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = (
            "id",
            "chat",
            "sender",
            "text",
            "created_at",
        )
