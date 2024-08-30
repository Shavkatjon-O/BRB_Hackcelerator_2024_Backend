from rest_framework import generics

from apps.chats.models import Chat, Message, User
from apps.chats.serializers import ChatSerializer, MessageSerializer, UserSerializer


# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class ChatListCreateView(generics.ListCreateAPIView):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer


# class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer


# class MessageListCreateView(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

#     def get_queryset(self):
#         chat_id = self.kwargs.get("chat_id")
#         return Message.objects.filter(chat_id=chat_id)


# class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        return Chat.objects.filter(users=self.request.user)


class ChatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.kwargs.get("chat_id")
        if chat_id:
            return Message.objects.filter(chat_id=chat_id)
        return Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
