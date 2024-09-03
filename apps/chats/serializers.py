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
