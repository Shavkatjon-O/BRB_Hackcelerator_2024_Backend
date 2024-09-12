from django.urls import path

from apps.cards.api.CardsList.views import CardsListView

urlpatterns = [
    path("", CardsListView.as_view(), name="cards-list"),
]
