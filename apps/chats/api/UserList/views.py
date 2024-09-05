from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserListSerializer
from apps.users.models import User
from apps.chats.models import Chat


class UserListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        current_user = self.request.user
        return User.objects.exclude(
            id__in=Chat.objects.filter(users=current_user).values_list(
                "users", flat=True
            )
        ).exclude(id=current_user.id)


__all__ = ("UserListView",)
