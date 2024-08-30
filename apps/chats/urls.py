# from django.urls import path
# from . import views

# urlpatterns = [
#     path("chats/", views.ChatListView.as_view(), name="chat-list"),
#     path("chats/<int:pk>/", views.ChatDetailView.as_view(), name="chat-detail"),
#     path(
#         "chats/<int:pk>/messages/", views.MessageListView.as_view(), name="message-list"
#     ),
#     path(
#         "chats/<int:pk>/messages/<int:message_pk>/",
#         views.MessageDetailView.as_view(),
#         name="message-detail",
#     ),
#     path("users/", views.UserListView.as_view(), name="user-list"),
#     path("users/<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
# ]


# urlpatterns = [
#     path("users/", views.UserListView.as_view(), name="user-list"),
# ]

# urls.py
# from django.urls import path
# from .views import (
#     ChatListCreateView,
#     ChatDetailView,
#     MessageListCreateView,
#     MessageDetailView,
#     UserListView,
# )

# urlpatterns = [
#     path("", ChatListCreateView.as_view(), name="chat-list-create"),
#     path("<int:pk>/", ChatDetailView.as_view(), name="chat-detail"),
#     path(
#         "<int:chat_id>/messages/",
#         MessageListCreateView.as_view(),
#         name="message-list-create",
#     ),
#     path("messages/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
#     path("users/", UserListView.as_view(), name="user-list"),
# ]

from django.urls import path

from apps.chats.views import (
    ChatListCreateView,
    ChatRetrieveUpdateDestroyView,
    MessageListCreateView,
    MessageRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("chats/", ChatListCreateView.as_view()),
    path("chats/<int:pk>/", ChatRetrieveUpdateDestroyView.as_view()),
    path("messages/", MessageListCreateView.as_view()),
    path("messages/<int:pk>/", MessageRetrieveUpdateDestroyView.as_view()),
]
