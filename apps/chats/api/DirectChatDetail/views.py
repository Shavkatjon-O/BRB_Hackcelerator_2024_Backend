from django.db.models import Q
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.chats.api.DirectChatDetail.serializers import DirectChatDetailSerializer
from apps.chats.models import DirectChat


class DirectChatDetailView(RetrieveAPIView):
    serializer_class = DirectChatDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return DirectChat.objects.filter(
            Q(user1=self.request.user) | Q(user2=self.request.user),
        ).select_related("user1", "user2")


__all__ = ("DirectChatDetailView",)
