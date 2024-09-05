from django.urls import path
from apps.chats.views import (
    UserListView,
    MessageListView,
    MessageDetailView,
    ChatListView,
    ChatDetailView,
)

urlpatterns = [
    path("users/", UserListView.as_view(), name="users"),
    path("chats/", ChatListView.as_view(), name="chats"),
    path("chats/<int:pk>/", ChatDetailView.as_view(), name="chat-detail"),
    path("chats/<int:chat_id>/messages/", MessageListView.as_view(), name="messages"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
]
