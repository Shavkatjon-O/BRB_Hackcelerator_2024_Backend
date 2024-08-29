from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel


User = get_user_model()


class Event(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=256)

    description = models.TextField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
