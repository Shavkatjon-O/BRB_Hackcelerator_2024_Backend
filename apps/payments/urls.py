from django.urls import path

from apps.payments.api.PaymentCreate.views import PaymentCreateAPIView
from apps.payments.api.PaymentDelete.views import PaymentDeleteAPIView
from apps.payments.api.PaymentDetail.views import PaymentDetailAPIView
from apps.payments.api.PaymentList.views import PaymentListAPIView
from apps.payments.api.PaymentUpdate.views import PaymentUpdateAPIView

urlpatterns = [
    path("", PaymentListAPIView.as_view(), name="payment-list"),
    path("create/", PaymentCreateAPIView.as_view(), name="payment-create"),
    path("delete/<int:pk>/", PaymentDeleteAPIView.as_view(), name="payment-delete"),
    path("detail/<int:pk>/", PaymentDetailAPIView.as_view(), name="payment-detail"),
    path("update/<int:pk>/", PaymentUpdateAPIView.as_view(), name="payment-update"),
]
