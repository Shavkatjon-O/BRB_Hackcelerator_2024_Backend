from django.db import models
from apps.common.models import BaseModel
from apps.clients.models import Client
from apps.users.models import User


class ApplicationStatusChoices(models.TextChoices):
    PENDING = "PENDING", "Pending"
    APPROVED = "APPROVED", "Approved"
    REJECTED = "REJECTED", "Rejected"
    UNDER_REVIEW = "UNDER_REVIEW", "Under Review"
    DISBURSED = "DISBURSED", "Disbursed"


class LoanTypeChoices(models.TextChoices):
    PERSONAL_LOAN = "PERSONAL_LOAN", "Personal Loan"
    BUSINESS_LOAN = "BUSINESS_LOAN", "Business Loan"
    MORTGAGE = "MORTGAGE", "Mortgage"
    STUDENT_LOAN = "STUDENT_LOAN", "Student Loan"
    CAR_LOAN = "CAR_LOAN", "Car Loan"


class CurrencyChoices(models.TextChoices):
    USD = "USD", "US Dollar"
    UZS = "UZS", "Uzbekistani Som"
    EUR = "EUR", "Euro"


class Application(BaseModel):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="applications"
    )
    loan_type = models.CharField(max_length=32, choices=LoanTypeChoices.choices)
    amount_requested = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(
        max_length=3, choices=CurrencyChoices.choices, default=CurrencyChoices.UZS
    )

    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=ApplicationStatusChoices.choices,
        default=ApplicationStatusChoices.PENDING,
    )

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_applications"
    )
    approved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="approved_applications",
        blank=True,
        null=True,
    )

    loan_purpose = models.TextField(blank=True, null=True)
    interest_rate = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    repayment_period_months = models.IntegerField(blank=True, null=True)
    reference_number = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"Application {self.reference_number} - {self.client} - {self.amount_requested} {self.currency}"

    class Meta:
        verbose_name = "Loan Application"
        verbose_name_plural = "Loan Applications"
        ordering = ["-created_at"]


class ApplicationSchedule(BaseModel):
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE, related_name="schedules"
    )
    due_date = models.DateField()
    installment_amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Installment {self.id} for Application {self.application.reference_number} due on {self.due_date}"

    class Meta:
        verbose_name = "Application Schedule"
        verbose_name_plural = "Application Schedules"
        ordering = ["due_date"]
