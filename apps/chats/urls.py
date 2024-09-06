from django.urls import path

from apps.chats.api.UserList import UserListView

from apps.chats.api.DirectChatCreate import DirectChatCreateView
from apps.chats.api.DirectChatDetail import DirectChatDetailView
from apps.chats.api.DirectChatList import DirectChatListView
from apps.chats.api.DirectMessageCreate import DirectMessageCreateView
from apps.chats.api.DirectMessageList import DirectMessageListView

from apps.chats.api.GroupChatDetail import GroupChatDetailView
from apps.chats.api.GroupChatList import GroupChatListView

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("directs/create/", DirectChatCreateView.as_view()),
    path("directs/", DirectChatListView.as_view()),
    path("directs/<int:pk>/", DirectChatDetailView.as_view()),
    path("directs/<int:pk>/messages/", DirectMessageListView.as_view()),
    path("groups/", GroupChatListView.as_view()),
    path("groups/<int:pk>/", GroupChatDetailView.as_view()),
]
