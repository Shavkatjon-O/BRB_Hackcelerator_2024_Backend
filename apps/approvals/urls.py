from django.urls import path
from apps.approvals.views import RequestCreateAPIView, RequestListAPIView

urlpatterns = [
    path("create/", RequestCreateAPIView.as_view(), name="create"),
    path("list/", RequestListAPIView.as_view(), name="list"),
]
