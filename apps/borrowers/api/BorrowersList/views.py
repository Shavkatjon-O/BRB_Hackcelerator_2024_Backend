from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.borrowers.api.BorrowersList.serializers import BorrowersListSerializer
from apps.borrowers.models import Borrower


class BorrowersListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BorrowersListSerializer
    queryset = Borrower.objects.all()


__all__ = ("BorrowersListAPIView",)
