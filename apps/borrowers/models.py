from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User


class BorrowerTypeChoices(models.TextChoices):
    INDIVIDUAL = "INDIVIDUAL", "Individual"
    COMPANY = "COMPANY", "Company"


class BorrowerStatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"
    BLACKLISTED = "BLACKLISTED", "Blacklisted"


class Borrower(BaseModel):
    borrower_type = models.CharField(max_length=32, choices=BorrowerTypeChoices.choices)
    full_name = models.CharField(max_length=255)  # For both individuals and companies
    date_of_birth = models.DateField(blank=True, null=True)  # Only for individuals
    identification_number = models.CharField(
        max_length=64, unique=True
    )  # National ID, tax number, etc.
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=32,
        choices=BorrowerStatusChoices.choices,
        default=BorrowerStatusChoices.ACTIVE,
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_borrowers"
    )
    approved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="approved_borrowers",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.full_name} ({self.borrower_type})"

    class Meta:
        verbose_name = "Borrower"
        verbose_name_plural = "Borrowers"
        ordering = ["full_name"]


class BorrowerFinancialInfo(BaseModel):
    borrower = models.OneToOneField(
        Borrower, on_delete=models.CASCADE, related_name="financial_info"
    )
    annual_income = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )  # Can apply for both individuals and companies
    credit_score = models.IntegerField(blank=True, null=True)
    total_outstanding_debt = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    total_loans = models.IntegerField(default=0)

    def __str__(self):
        return f"Financial Info for {self.borrower.full_name}"

    class Meta:
        verbose_name = "Borrower Financial Info"
        verbose_name_plural = "Borrower Financial Infos"


class BorrowerDocument(BaseModel):
    borrower = models.ForeignKey(
        Borrower, on_delete=models.CASCADE, related_name="documents"
    )
    document_type = models.CharField(
        max_length=64
    )  # E.g., Passport, Tax Document, Utility Bill, etc.
    document_number = models.CharField(max_length=128)
    document_file = models.FileField(upload_to="borrower_documents/")
    expiration_date = models.DateField(blank=True, null=True)
    issued_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.document_type} for {self.borrower.full_name}"

    class Meta:
        verbose_name = "Borrower Document"
        verbose_name_plural = "Borrower Documents"
        ordering = ["document_type"]
