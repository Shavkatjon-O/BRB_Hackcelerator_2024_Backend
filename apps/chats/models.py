from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel

User = get_user_model()


class Chat(BaseModel):
    users = models.ManyToManyField(User, related_name="chats")
    title = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(upload_to="groups/", null=True, blank=True)
    is_group = models.BooleanField(default=False)

    def __str__(self):
        return self.title or f"Private chat {self.id}"

    def save(self, *args, **kwargs):
        if not self.is_group and self.users.count() > 2:
            raise ValueError("Private chat can't have more than 2 users")
        super().save(*args, **kwargs)


class Message(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages"
    )  # sender
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name="messages"
    )  # receiver
    text = models.TextField()

    def __str__(self):
        return self.text
