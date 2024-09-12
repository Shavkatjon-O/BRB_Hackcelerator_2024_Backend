from django.urls import path

from apps.payments.api.PaymentCreate.views import PaymentCreateAPIView

urlpatterns = [
    path("create/", PaymentCreateAPIView.as_view(), name="payment-create"),
]
