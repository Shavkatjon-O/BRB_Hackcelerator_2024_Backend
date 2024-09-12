from django.db import models
from apps.common.models import BaseModel
from apps.clients.models import Client
from apps.users.models import User


class LoanStatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    PAID_OFF = "PAID_OFF", "Paid Off"
    DEFAULTED = "DEFAULTED", "Defaulted"
    CLOSED = "CLOSED", "Closed"
    UNDER_REVIEW = "UNDER_REVIEW", "Under Review"
    PENDING_DISBURSEMENT = "PENDING_DISBURSEMENT", "Pending Disbursement"


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


class Loan(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="loans")
    loan_type = models.CharField(max_length=32, choices=LoanTypeChoices.choices)
    amount_disbursed = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(
        max_length=3, choices=CurrencyChoices.choices, default=CurrencyChoices.UZS
    )
    disbursement_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=32,
        choices=LoanStatusChoices.choices,
        default=LoanStatusChoices.PENDING_DISBURSEMENT,
    )
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    repayment_period_months = models.IntegerField()
    total_amount_due = models.DecimalField(max_digits=12, decimal_places=2)
    reference_number = models.CharField(max_length=128, unique=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_loans"
    )
    approved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="approved_loans",
        blank=True,
        null=True,
    )

    is_over_due = models.BooleanField(default=False)

    def __str__(self):
        return f"Loan {self.reference_number} - {self.client} - {self.amount_disbursed} {self.currency}"

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
        ordering = ["-created_at"]


class LoanRepaymentSchedule(BaseModel):
    loan = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name="repayment_schedules"
    )
    due_date = models.DateField()
    installment_amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Installment {self.id} for Loan {self.loan.reference_number} due on {self.due_date}"

    class Meta:
        verbose_name = "Loan Repayment Schedule"
        verbose_name_plural = "Loan Repayment Schedules"
        ordering = ["due_date"]
