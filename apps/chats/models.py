from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel

User = get_user_model()


class Chat(BaseModel):
    title = models.CharField(max_length=256)
    users = models.ManyToManyField(User, related_name="chats")

    def __str__(self):
        return self.title


class Message(BaseModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()

    def __str__(self):
        return self.text
