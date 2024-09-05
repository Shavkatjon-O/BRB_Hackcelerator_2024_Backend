from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import DirectChatDetailSerializer
from apps.chats.models import Chat


class DirectChatDetailView(RetrieveAPIView):
    serializer_class = DirectChatDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(users=self.request.user, is_group=False)


__all__ = ("DirectChatDetailView",)
