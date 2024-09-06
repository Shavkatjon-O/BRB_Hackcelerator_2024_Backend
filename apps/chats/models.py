from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User


class DirectChat(BaseModel):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user1", "user2")


class DirectMessage(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(DirectChat, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class GroupChat(BaseModel):
    users = models.ManyToManyField(User, related_name="group_chats")
    image = models.ImageField(upload_to="groups", null=True, blank=True)
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class GroupMessage(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
