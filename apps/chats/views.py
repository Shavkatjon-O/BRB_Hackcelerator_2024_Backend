from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.chats.models import Chat, Message
from apps.chats.serializers import UserSerializer
from apps.users.models import User


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
