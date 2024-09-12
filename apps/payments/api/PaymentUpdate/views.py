from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payments.api.PaymentUpdate.serializers import PaymentUpdateSerializer
from apps.payments.models import Payment


class PaymentUpdateAPIView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentUpdateSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ("PaymentUpdateAPIView",)
