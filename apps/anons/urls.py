from django.urls import path

from apps.anons.api.AnonsList.views import AnonsListView
from apps.anons.api.AnonsDetail.views import AnonsDetailView

urlpatterns = [
    path("", AnonsListView.as_view(), name="anons-list"),
    path("<int:pk>/", AnonsDetailView.as_view(), name="anons-detail"),
]
