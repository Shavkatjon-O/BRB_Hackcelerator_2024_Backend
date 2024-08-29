from rest_framework import generics
from apps.chats import serializers, models


class UserListView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class ChatListView(generics.ListCreateAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer


class ChatDetailView(generics.RetrieveAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer


class MessageListView(generics.ListAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer


class MessageDetailView(generics.RetrieveAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
