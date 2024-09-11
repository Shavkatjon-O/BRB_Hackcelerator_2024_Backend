from django.db import models
from apps.common.models import BaseModel


class ClientGenderChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHER = "O", "Other"


class Client(BaseModel):
    full_name = models.CharField(max_length=256)

    gender = models.CharField(
        max_length=1,
        choices=ClientGenderChoices.choices,
        default=ClientGenderChoices.OTHER,
    )
    email = models.EmailField(unique=True)

    birth_date = models.DateField()
    phone_number = models.CharField(max_length=32, unique=True)
    city = models.CharField(max_length=128)
    postal_code = models.CharField(max_length=32)
    country = models.CharField(max_length=128)
    address = models.TextField()

    identification_number = models.CharField(max_length=64, unique=True)
    credit_score = models.IntegerField(blank=True, null=True)

    image = models.ImageField(upload_to="clients", blank=True, null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
