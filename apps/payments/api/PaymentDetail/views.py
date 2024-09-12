from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payments.api.PaymentDetail.serializers import PaymentDetailSerializer
from apps.payments.models import Payment


class PaymentDetailAPIView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentDetailSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ("PaymentDetailAPIView",)
