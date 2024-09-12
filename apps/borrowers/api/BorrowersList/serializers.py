from rest_framework import serializers
from apps.borrowers.models import Borrower


class BorrowersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = "__all__"


__all__ = ("BorrowersListSerializer",)
