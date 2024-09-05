from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import GroupChatDetailSerializer
from apps.chats.models import Chat


class GroupChatDetailView(RetrieveAPIView):
    serializer_class = GroupChatDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(users=self.request.user, is_group=True)


__all__ = ("GroupChatDetailView",)
