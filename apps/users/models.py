from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.common.models import BaseModel
from apps.users.managers import UserManager


class UserTypeChoices(models.TextChoices):
    EMPLOYEE = "EMPLOYEE", "Employee"
    LOAN_MANAGER = "LOAN_MANAGER", "Loan Manager"
    BANK_TELLER = "BANK_TELLER", "Bank Teller"


class User(AbstractUser, BaseModel):
    username = None

    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=126, null=True, blank=True)
    last_name = models.CharField(max_length=126, null=True, blank=True)
    phone_number = models.CharField(max_length=32, null=True, blank=True)

    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    job_title = models.CharField(max_length=126, null=True, blank=True)
    department = models.CharField(max_length=126, null=True, blank=True)
    education = models.CharField(max_length=256, null=True, blank=True)

    employment_start_date = models.DateField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to="users/", null=True, blank=True)

    user_type = models.CharField(
        max_length=32, choices=UserTypeChoices.choices, default=UserTypeChoices.EMPLOYEE
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email
