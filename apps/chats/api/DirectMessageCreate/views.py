from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import DirectMessageCreateSerializer


class DirectMessageCreateView(CreateAPIView):
    serializer_class = DirectMessageCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


__all__ = ("DirectMessageCreateView",)
