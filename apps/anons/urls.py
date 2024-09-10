from django.urls import path

from apps.anons.api.AnonsList.views import AnonsListView

urlpatterns = [
    path("", AnonsListView.as_view(), name="anons-list"),
]
