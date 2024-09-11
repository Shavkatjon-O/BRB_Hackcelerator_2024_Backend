from django.urls import path

from apps.clients.api.ClientsList import ClientsListAPIView

urlpatterns = [
    path("", ClientsListAPIView.as_view(), name="clients-list"),
]
