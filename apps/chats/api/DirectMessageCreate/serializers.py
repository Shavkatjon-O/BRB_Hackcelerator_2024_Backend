from rest_framework import serializers
from apps.chats.models import DirectMessage


class DirectMessageCreateSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=1000)
    chat_id = serializers.IntegerField()

    class Meta:
        model = DirectMessage
        fields = (
            "text",
            "chat_id",
        )


__all__ = ("DirectMessageCreateSerializer",)
