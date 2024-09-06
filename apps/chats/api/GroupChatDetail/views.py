from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import GroupChatDetailSerializer
from apps.chats.models import GroupChat


class GroupChatDetailView(RetrieveAPIView):
    serializer_class = GroupChatDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return GroupChat.objects.filter(users=self.request.usere)


__all__ = ("GroupChatDetailView",)
