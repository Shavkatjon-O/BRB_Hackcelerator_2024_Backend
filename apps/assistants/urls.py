from django.urls import path


from .views import ChatView

urlpatterns = [
    path("chat-support/", ChatView.as_view(), name="chat"),
]
