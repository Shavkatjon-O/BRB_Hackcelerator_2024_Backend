from django.urls import path
from apps.messages import views

urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("chats/", views.ChatListView.as_view(), name="chat-list"),
    path("chats/<int:pk>/", views.ChatDetailView.as_view(), name="chat-detail"),
    path(
        "chats/<int:chat_id>/messages/",
        views.MessageListCreateView.as_view(),
        name="message-list-create",
    ),
]
