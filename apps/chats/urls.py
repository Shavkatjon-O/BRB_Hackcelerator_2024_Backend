from django.urls import path
from apps.chats import views

urlpatterns = [
    path("users/", views.UserListView.as_view(), name="users-list"),
    path("chats/", views.ChatListView.as_view(), name="chats-list"),
    path("chats/create/", views.ChatCreateView.as_view(), name="chat-create"),
    path("chats/<int:pk>/", views.ChatDetailView.as_view(), name="chat-detail"),
    path(
        "chats/<int:chat_id>/messages/",
        views.MessageListView.as_view(),
        name="messages-list",
    ),
    path(
        "chats/<int:chat_id>/messages/create/",
        views.MessageCreateView.as_view(),
        name="message-create",
    ),
    path(
        "chats/<int:chat_id>/messages/<int:pk>/",
        views.MessageDetailView.as_view(),
        name="message-detail",
    ),
]
