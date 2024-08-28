from rest_framework import generics
from apps.messages.models import Chat, Message
from apps.messages.serializers import ChatSerializer, MessageSerializer


# List all chats or create a new chat
class ChatListView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


# Retrieve a specific chat
class ChatDetailView(generics.RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


# List or create messages in a specific chat
class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(chat_id=self.kwargs["chat_id"])

    def perform_create(self, serializer):
        chat = Chat.objects.get(pk=self.kwargs["chat_id"])
        serializer.save(chat=chat, sender=self.request.user)
