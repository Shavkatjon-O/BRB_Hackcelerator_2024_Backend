from django.urls import path
from .views import (
    CalendarListCreateView,
    CalendarRetrieveUpdateDestroyView,
    EventListCreateView,
    EventRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("calendars/", CalendarListCreateView.as_view(), name="calendar-list-create"),
    path(
        "calendars/<int:pk>/",
        CalendarRetrieveUpdateDestroyView.as_view(),
        name="calendar-detail",
    ),
    path(
        "calendars/<int:calendar_id>/events/",
        EventListCreateView.as_view(),
        name="event-list-create",
    ),
    path(
        "calendars/<int:calendar_id>/events/<int:pk>/",
        EventRetrieveUpdateDestroyView.as_view(),
        name="event-detail",
    ),
]
