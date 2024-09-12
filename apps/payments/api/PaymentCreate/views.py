from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payments.api.PaymentCreate.serializers import PaymentCreateSerializer
from apps.payments.models import Payment


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


__all__ = ("PaymentCreateAPIView",)
