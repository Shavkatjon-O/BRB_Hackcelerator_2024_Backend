from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payments.api.PaymentList.serializers import PaymentListSerializer
from apps.payments.models import Payment


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ("PaymentListAPIView",)
