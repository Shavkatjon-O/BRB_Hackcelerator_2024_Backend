from django.urls import path
from apps.approvals.views import RequestCreateAPIView, RequestListAPIView

urlpatterns = [
    path("", RequestListAPIView.as_view(), name="list"),
    path("create/", RequestCreateAPIView.as_view(), name="create"),
]
