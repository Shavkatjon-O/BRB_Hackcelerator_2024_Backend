from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payments.api.PaymentDelete.serializers import PaymentDeleteSerializer
from apps.payments.models import Payment


class PaymentDeleteAPIView(DestroyAPIView):
    serializer_class = PaymentDeleteSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Payment.objects.all()


__all__ = ("PaymentDeleteAPIView",)
