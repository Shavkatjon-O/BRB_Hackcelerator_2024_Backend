from django.urls import path

from apps.applications.api.ApplicationsList.views import ApplicationsListAPIView

urlpatterns = [
    path("", ApplicationsListAPIView.as_view(), name="applications-list"),
]
