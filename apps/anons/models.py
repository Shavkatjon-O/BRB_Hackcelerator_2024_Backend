from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User


class Anons(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()

    read_by = models.ManyToManyField(
        User, related_name="read_anons", null=True, blank=True
    )

    class Meta:
        verbose_name = "Anons"
        verbose_name_plural = "Anons"

    def __str__(self):
        return self.title
