from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User


class Anons(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()

    class Meta:
        verbose_name = "Anons"
        verbose_name_plural = "Anons"

    def __str__(self):
        return self.title


class AnonsReader(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anons = models.ForeignKey(Anons, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "anons")

    def __str__(self):
        return f"{self.user} - {self.anons}"
