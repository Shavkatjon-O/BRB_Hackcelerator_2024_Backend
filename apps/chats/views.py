from rest_framework import generics
from apps.chats import models, serializers


class UserListView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class ChatListView(generics.ListAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer

    def get_queryset(self):
        return self.queryset.filter(users=self.request.user)


class ChatCreateView(generics.CreateAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])


class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer

    def get_queryset(self):
        return self.queryset.filter(users=self.request.user)


class MessageListView(generics.ListAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        return self.queryset.filter(chat=self.kwargs["chat_id"])


class MessageCreateView(generics.CreateAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        return self.queryset.filter(chat=self.kwargs["chat_id"])
