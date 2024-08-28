from rest_framework import viewsets
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


# class ChatViewSet(RetrieveAPIView):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer


class ChatViewSet(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.kwargs["chat_id"]

        print(self.queryset.filter(chat__id=chat_id))
        return self.queryset.filter(chat__id=chat_id)
