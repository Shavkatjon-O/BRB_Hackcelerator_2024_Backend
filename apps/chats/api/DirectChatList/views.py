# from django.db.models import Q
# from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAuthenticated

# from apps.chats.api.DirectChatList.serializers import DirectChatListSerializer
# from apps.chats.models import DirectChat


# class DirectChatListView(ListAPIView):
#     serializer_class = DirectChatListSerializer
#     permission_classes = (IsAuthenticated,)

#     def get_queryset(self):
#         return DirectChat.objects.filter(
#             Q(user1=self.request.user) | Q(user2=self.request.user),
#         ).select_related("user1", "user2")


# __all__ = ("DirectChatListView",)


from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from apps.chats.api.DirectChatList.serializers import DirectChatListSerializer
from apps.chats.models import DirectChat
from django.db.models import Q


class DirectChatListPagination(LimitOffsetPagination):
    default_limit = 20  # Default number of messages to return per page
    max_limit = 100  # Maximum number of messages to return per request


class DirectChatListView(ListAPIView):
    serializer_class = DirectChatListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = DirectChatListPagination  # Add pagination

    def get_queryset(self):
        return DirectChat.objects.filter(
            Q(user1=self.request.user) | Q(user2=self.request.user),
        ).select_related("user1", "user2")


__all__ = ("DirectChatListView",)
