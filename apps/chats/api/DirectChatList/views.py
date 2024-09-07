from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.chats.api.DirectChatList.serializers import DirectChatListSerializer
from apps.chats.models import DirectChat


class DirectChatListView(ListAPIView):
    serializer_class = DirectChatListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return DirectChat.objects.filter(
            Q(user1=self.request.user) | Q(user2=self.request.user),
        ).select_related("user1", "user2")


__all__ = ("DirectChatListView",)
