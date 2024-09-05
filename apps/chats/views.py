from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.chats.models import Chat, Message
from apps.chats.serializers import (
    UserSerializer,
    ChatSerializer,
    MessageSerializer,
    ChatDetailSerializer,
)
from apps.users.models import User


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ChatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_authenticated:
            return Chat.objects.filter(users=user)
        return Chat.objects.none()


class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class MessageListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get_queryset(self):
        chat_id = self.kwargs["chat_id"]
        return Message.objects.filter(chat_id=chat_id)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class ChatRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChatDetailSerializer
    queryset = Chat.objects.all()
