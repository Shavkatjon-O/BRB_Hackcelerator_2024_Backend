from django.db import models
from django.contrib.auth import get_user_model

from apps.common.models import BaseModel

User = get_user_model()


class Chat(BaseModel):
    participants = models.ManyToManyField(User, related_name="chats")
    last_message = models.OneToOneField(
        "Message",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"Chat {self.id}"


class Message(BaseModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()

    def __str__(self):
        return f"Message {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.chat.last_message = self
        self.chat.save()
