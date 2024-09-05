from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserListSerializer
from apps.users.models import User


class UsersListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)


__all__ = ("UsersListView",)
