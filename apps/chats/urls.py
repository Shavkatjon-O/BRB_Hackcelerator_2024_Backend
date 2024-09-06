from django.urls import path

from apps.chats.api.UserList import UserListView

from apps.chats.api.DirectChatCreate import DirectChatCreateView
from apps.chats.api.DirectChatDetail import DirectChatDetailView
from apps.chats.api.DirectChatList import DirectChatListView

# from apps.chats.api.GroupChatDetail import GroupChatDetailView
# from apps.chats.api.GroupChatList import GroupChatListView
# from apps.chats.api.MessageCreate import MessageCreateView
# from apps.chats.api.MessageList import MessageListView

urlpatterns = [
    path("users/", UserListView.as_view(), name="users"),
    path("direct/create/", DirectChatCreateView.as_view(), name="direct-chat-create"),
    path("direct/", DirectChatListView.as_view(), name="direct-chats"),
    # path("direct/<int:pk>/", DirectChatDetailView.as_view(), name="direct-chat-detail"),
    # path("group/", GroupChatListView.as_view(), name="group-chats"),
    # path("group/<int:pk>/", GroupChatDetailView.as_view(), name="group-chat-detail"),
    # path("messages/create/", MessageCreateView.as_view(), name="message-create"),
    # path("messages/<chat_id>/", MessageListView.as_view(), name="messages"),
]
