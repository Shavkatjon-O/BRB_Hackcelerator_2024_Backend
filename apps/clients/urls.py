from django.urls import path

from apps.clients.api.ClientsList.views import ClientsListAPIView
from apps.clients.api.ClientsCreate.views import ClientsCreateAPIView
from apps.clients.api.ClientsDetail.views import ClientsDetailAPIView
from apps.clients.api.ClientsUpdate.views import ClientsUpdateAPIView
from apps.clients.api.ClientsDelete.views import ClientsDeleteAPIView

urlpatterns = [
    path("", ClientsListAPIView.as_view(), name="clients-list"),
    path("create/", ClientsCreateAPIView.as_view(), name="clients-create"),
    path("<int:pk>/", ClientsDetailAPIView.as_view(), name="clients-detail"),
    path("<int:pk>/update/", ClientsUpdateAPIView.as_view(), name="clients-update"),
    path("<int:pk>/delete/", ClientsDeleteAPIView.as_view(), name="clients-delete"),
]
