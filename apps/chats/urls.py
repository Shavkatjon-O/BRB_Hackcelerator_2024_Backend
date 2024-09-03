from django.urls import path
from apps.chats.views import UserListView

urlpatterns = [
    path("users/", UserListView.as_view(), name="users"),
]
