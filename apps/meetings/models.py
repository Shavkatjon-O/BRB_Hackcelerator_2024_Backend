from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User


class Meeting(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
