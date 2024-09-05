from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import GroupChatListSerializer
from apps.chats.models import Chat


class GroupChatListView(ListAPIView):
    serializer_class = GroupChatListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(users=self.request.user, is_group=True)


__all__ = ("GroupChatListView",)
