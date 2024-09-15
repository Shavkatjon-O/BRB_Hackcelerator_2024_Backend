from django.urls import path
from .models import DesktopDownloadDetailView, MobileDownloadDetailView

urlpatterns = [
    path(
        "downloads/desktop/",
        DesktopDownloadDetailView.as_view(),
        name="desktop-download",
    ),
    path(
        "downloads/mobile/", MobileDownloadDetailView.as_view(), name="mobile-download"
    ),
]
