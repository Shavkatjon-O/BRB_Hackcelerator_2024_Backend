from django.db import models
from apps.common.models import BaseModel
from apps.clients.models import Client
from apps.users.models import User

from django.db import models


class PaymentStatusChoices(models.TextChoices):
    PENDING = "PENDING", "Pending"
    COMPLETED = "COMPLETED", "Completed"
    REJECTED = "REJECTED", "Rejected"


class PaymentTypeChoices(models.TextChoices):
    LOAN_REPAYMENT = "LOAN_REPAYMENT", "Loan Repayment"
    INSTALLMENT_PAYMENT = "INSTALLMENT_PAYMENT", "Installment Payment"
    INTEREST_PAYMENT = "INTEREST_PAYMENT", "Interest Payment"
    PRINCIPAL_PAYMENT = "PRINCIPAL_PAYMENT", "Principal Payment"
    PENALTY_PAYMENT = "PENALTY_PAYMENT", "Penalty Payment"
    ADVANCE_PAYMENT = "ADVANCE_PAYMENT", "Advance Payment"
    REFUND = "REFUND", "Refund"
    RESTRUCTURED_PAYMENT = "RESTRUCTURED_PAYMENT", "Restructured Payment"


class PaymentMethodChoices(models.TextChoices):
    CASH = "CASH", "Cash"
    BANK_TRANSFER = "BANK_TRANSFER", "Bank Transfer"
    MOBILE_MONEY = "MOBILE_MONEY", "Mobile Money"
    POS = "POS", "POS Terminal"
    ONLINE_PAYMENT = "ONLINE_PAYMENT", "Online Payment"


class CurrencyChoices(models.TextChoices):
    USD = "USD", "US Dollar"
    UZS = "UZS", "Uzbekistani Som"
    EUR = "EUR", "Euro"


class Payment(BaseModel):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="payments"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(
        max_length=3, choices=CurrencyChoices.choices, default=CurrencyChoices.UZS
    )

    payment_type = models.CharField(max_length=20, choices=PaymentTypeChoices.choices)
    payment_method = models.CharField(
        max_length=20, choices=PaymentMethodChoices.choices
    )

    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_payments"
    )
    approved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="approved_payments",
        blank=True,
        null=True,
    )

    reference_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20,
        choices=PaymentStatusChoices.choices,
        default=PaymentStatusChoices.PENDING,
    )

    def __str__(self):
        return f"Payment {self.reference_number} - {self.client} - {self.amount} {self.currency}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ["-created_at"]


class PaymentSchedule(BaseModel):
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="schedules"
    )
    due_date = models.DateField()
    installment_amount = models.DecimalField(max_digits=12, decimal_places=2)

    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Installment {self.id} for Payment {self.payment.reference_number} due on {self.due_date}"

    class Meta:
        verbose_name = "Payment Schedule"
        verbose_name_plural = "Payment Schedules"
        ordering = ["due_date"]
