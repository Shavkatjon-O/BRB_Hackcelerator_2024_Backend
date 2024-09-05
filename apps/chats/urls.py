# from django.urls import path
# from apps.chats.views import (
#     UserListView,
#     MessageListView,
#     MessageDetailView,
#     ChatListView,
#     ChatDetailView,
# )

# urlpatterns = [
#     path("users/", UserListView.as_view(), name="users"),
#     path("chats/", ChatListView.as_view(), name="chats"),
#     path("chats/<int:pk>/", ChatDetailView.as_view(), name="chat-detail"),
#     path("chats/<int:chat_id>/messages/", MessageListView.as_view(), name="messages"),
#     path("messages/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
# ]

from django.urls import path

from apps.chats.api.UsersList import UsersListView
from apps.chats.api.MessageCreate import MessageCreateView
from apps.chats.api.MessagesList import MessagesListView

from apps.chats.views import UserListView

urlpatterns = [
    path("users/", UsersListView.as_view(), name="users"),
    path("messages/create/", MessageCreateView.as_view(), name="message-create"),
    path("messages/", MessagesListView.as_view(), name="messages"),
    path("<int:pk>/", UserListView.as_view(), name="users"),
]
