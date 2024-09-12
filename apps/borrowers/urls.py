from django.urls import path

from apps.borrowers.api.BorrowersList.views import BorrowersListAPIView

urlpatterns = [
    path("", BorrowersListAPIView.as_view(), name="borrowers-list"),
]
