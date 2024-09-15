from rest_framework import serializers
from apps.loans.models import Loan

from apps.clients.api.ClientsDetail.serializers import ClientDetailSerializer


class LoansListSerializer(serializers.ModelSerializer):
    client = ClientDetailSerializer()

    class Meta:
        model = Loan
        fields = "__all__"


__all__ = ("LoansListSerializer",)
