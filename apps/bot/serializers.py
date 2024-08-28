from rest_framework import serializers
from .models import ChatBot


class ChatSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=200, write_only=True)
    answer = serializers.CharField(read_only=True)

    class Meta:
        model = ChatBot
        fields = ["question", "answer"]
