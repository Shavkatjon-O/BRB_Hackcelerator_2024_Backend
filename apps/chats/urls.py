from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r"chats", views.ChatViewSet)
# router.register(r"messages", views.MessageViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]


urlpatterns = [
    path("chats/<int:pk>/", views.ChatViewSet.as_view(), name="chat"),
    path("messages/<int:pk>/", views.MessageViewSet.as_view(), name="message"),
]
