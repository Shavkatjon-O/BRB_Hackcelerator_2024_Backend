from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .serializers import DirectChatCreateSerializer
from apps.chats.models import Chat


class DirectChatCreateView(CreateAPIView):
    serializer_class = DirectChatCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        users = serializer.validated_data.get("users")

        if len(users) != 1:
            raise ValidationError("Private chat must include exactly one other user.")

        chat = Chat.objects.create(is_group=False)
        chat.users.add(self.request.user, *users)

        serializer.instance = chat
        return chat


__all__ = ("DirectChatCreateView",)
