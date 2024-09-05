from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import DirectChatListSerializer
from apps.chats.models import Chat


class DirectChatListView(ListAPIView):
    serializer_class = DirectChatListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(users=self.request.user, is_group=False)


__all__ = ("DirectChatListView",)
