from .views import DistributionView

from django.urls import path

urlpatterns = [
    path("distribution/", DistributionView.as_view(), name="distribution"),
]
