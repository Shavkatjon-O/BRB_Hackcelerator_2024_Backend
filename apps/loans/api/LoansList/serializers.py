from rest_framework import serializers
from apps.loans.models import Loan


class LoansListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"


__all__ = ("LoansListSerializer",)
