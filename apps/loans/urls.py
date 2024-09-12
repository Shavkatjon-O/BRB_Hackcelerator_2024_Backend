from django.urls import path

from apps.loans.api.LoansList.views import LoansListAPIView

urlpatterns = [
    path("", LoansListAPIView.as_view(), name="loans-list"),
]
