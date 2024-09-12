from rest_framework import serializers
from apps.payments.models import Payment


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "id",
            "amount",
            "currency",
            "payment_type",
            "payment_method",
            "date",
            "description",
            "created_by",
            "approved_by",
            "reference_number",
            "status",
        )


__all__ = ("PaymentCreateSerializer",)
