from rest_framework import serializers
from apps.users.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
        )


__all__ = ("UserListSerializer",)
