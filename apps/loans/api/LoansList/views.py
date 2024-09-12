from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.loans.api.LoansList.serializers import LoansListSerializer
from apps.loans.models import Loan


class LoansListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LoansListSerializer
    queryset = Loan.objects.all()


__all__ = ("LoansListAPIView",)
