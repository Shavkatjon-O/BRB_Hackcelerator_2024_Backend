from django.urls import path
from .models import DesktopDownloadDetailView, MobileDownloadDetailView

urlpatterns = [
    path("desktop/", DesktopDownloadDetailView.as_view(), name="desktop-download"),
    path("mobile/", MobileDownloadDetailView.as_view(), name="mobile-download"),
]
