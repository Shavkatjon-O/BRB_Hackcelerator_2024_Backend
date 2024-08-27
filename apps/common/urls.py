from .views import DistributionView

from django.urls import path

urlpatterns = [
    path("desktop/<int:pk>/", DistributionView.as_view(), name="distribution"),
]
