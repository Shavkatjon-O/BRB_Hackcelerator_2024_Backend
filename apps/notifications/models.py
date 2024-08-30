from django.db import models
from apps.common.models import BaseModel


class Notification(BaseModel):
    message = models.CharField(max_length=256)

    def __str__(self):
        return self.message
