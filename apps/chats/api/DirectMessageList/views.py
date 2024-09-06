from rest_framework.generics import ListAPIView
from .serializers import DirectMessageListSerializer
from apps.chats.models import DirectMessage


class DirectMessageListView(ListAPIView):
    serializer_class = DirectMessageListSerializer

    def get_queryset(self):
        return DirectMessage.objects.filter(chat_id=self.kwargs["pk"])


__all__ = ("DirectMessageListView",)
