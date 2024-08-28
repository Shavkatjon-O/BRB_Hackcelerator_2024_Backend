from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel

User = get_user_model()


class Calendar(BaseModel):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="calendars"
    )
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Event(BaseModel):
    calendar = models.ForeignKey(
        Calendar, on_delete=models.CASCADE, related_name="events"
    )

    title = models.CharField(max_length=256)

    description = models.TextField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
