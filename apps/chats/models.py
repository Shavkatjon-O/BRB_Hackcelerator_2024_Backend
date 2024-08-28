from django.db import models
from django.contrib.auth import get_user_model

from apps.common.models import BaseModel

User = get_user_model()


class Chat(BaseModel):
    title = models.CharField(max_length=256, blank=True, null=True)
    is_group = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name="chats")

    def __str__(self):
        return self.title


class Message(BaseModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")

    content = models.TextField()

    def __str__(self):
        return self.content
