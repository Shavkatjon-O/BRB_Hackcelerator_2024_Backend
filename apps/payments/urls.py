from django.urls import path

from apps.payments.api.PaymentCreate.views import PaymentCreateAPIView
from apps.payments.api.PaymentDelete.views import PaymentDeleteAPIView

urlpatterns = [
    path("create/", PaymentCreateAPIView.as_view(), name="payment-create"),
    path("delete/<int:pk>/", PaymentDeleteAPIView.as_view(), name="payment-delete"),
]
