from django.db import models
from apps.common.models import BaseModel
from apps.clients.models import Client
from apps.users.models import User


class CardStatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    BLOCKED = "BLOCKED", "Blocked"
    EXPIRED = "EXPIRED", "Expired"
    PENDING_ACTIVATION = "PENDING_ACTIVATION", "Pending Activation"
    REPLACED = "REPLACED", "Replaced"
    CLOSED = "CLOSED", "Closed"


class CardTypeChoices(models.TextChoices):
    DEBIT = "DEBIT", "Debit"
    CREDIT = "CREDIT", "Credit"
    PREPAID = "PREPAID", "Prepaid"
    VIRTUAL = "VIRTUAL", "Virtual"
    CORPORATE = "CORPORATE", "Corporate"


class CurrencyChoices(models.TextChoices):
    USD = "USD", "US Dollar"
    UZS = "UZS", "Uzbekistani Som"
    EUR = "EUR", "Euro"


class Card(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="cards")
    card_number = models.CharField(max_length=16, unique=True)
    card_type = models.CharField(max_length=16, choices=CardTypeChoices.choices)
    currency = models.CharField(
        max_length=3, choices=CurrencyChoices.choices, default=CurrencyChoices.UZS
    )
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=32,
        choices=CardStatusChoices.choices,
        default=CardStatusChoices.PENDING_ACTIVATION,
    )
    expiration_date = models.DateField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_cards"
    )
    approved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="approved_cards",
        blank=True,
        null=True,
    )

    def __str__(self):
        return (
            f"Card {self.card_number} - {self.client} - {self.balance} {self.currency}"
        )

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
        ordering = ["-created_at"]


class CardTransaction(BaseModel):
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE, related_name="transactions"
    )
    transaction_amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_date = models.DateField(auto_now_add=True)
    transaction_type = models.CharField(
        max_length=50
    )  # e.g., Purchase, Withdrawal, Deposit
    merchant_details = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"Transaction {self.id} for Card {self.card.card_number} on {self.transaction_date}"

    class Meta:
        verbose_name = "Card Transaction"
        verbose_name_plural = "Card Transactions"
        ordering = ["-transaction_date"]
