from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .serializers import DirectChatCreateSerializer
from apps.chats.models import DirectChat


class DirectChatCreateView(CreateAPIView):
    serializer_class = DirectChatCreateSerializer
    permission_classes = (IsAuthenticated,)
    queryset = DirectChat.objects.all()


__all__ = ("DirectChatCreateView",)
