from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import GroupChatListSerializer
from apps.chats.models import GroupChat


class GroupChatListView(ListAPIView):
    serializer_class = GroupChatListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return GroupChat.objects.filter(users=self.request.user)


__all__ = ("GroupChatListView",)
