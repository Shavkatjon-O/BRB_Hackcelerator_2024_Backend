from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MessageCreateSerializer


class MessageCreateView(CreateAPIView):
    serializer_class = MessageCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


__all__ = ("MessageCreateView",)
