from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserListSerializer
from apps.chats.models import DirectChat
from apps.users.models import User


class UserListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserListSerializer

    def get_queryset(self):
        current_user = self.request.user

        exclude_users = (
            DirectChat.objects.filter(
                Q(user1=current_user.id) | Q(user2=current_user.id)
            )
            .values_list("user1", "user2")
            .flat()
        )
        return User.objects.exclude(
            id__in=exclude_users,
        ).exclude(
            id=current_user.id,
        )


__all__ = ("UserListView",)
