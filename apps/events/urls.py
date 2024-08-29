from django.urls import path
from apps.events import views

urlpatterns = [
    path("", views.EventListRetrieveView.as_view(), name="event-list"),
    path("create/", views.EventCreateView.as_view(), name="event-create"),
    path("<int:pk>/", views.EventRetrieveView.as_view(), name="event-retrieve"),
    path("<int:pk>/update/", views.EventUpdateView.as_view(), name="event-update"),
    path("<int:pk>/delete/", views.EventDestroyView.as_view(), name="event-delete"),
]
