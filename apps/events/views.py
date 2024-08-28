from rest_framework import generics
from .models import Calendar, Event
from .serializers import CalendarSerializer, EventSerializer


class CalendarListCreateView(generics.ListCreateAPIView):
    serializer_class = CalendarSerializer

    def get_queryset(self):
        return Calendar.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CalendarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CalendarSerializer

    def get_queryset(self):
        return Calendar.objects.filter(user=self.request.user)


class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        calendar_id = self.kwargs["calendar_id"]
        return Event.objects.filter(
            calendar__user=self.request.user, calendar_id=calendar_id
        )

    def perform_create(self, serializer):
        calendar_id = self.kwargs["calendar_id"]
        calendar = Calendar.objects.get(id=calendar_id, user=self.request.user)
        serializer.save(calendar=calendar)


class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        calendar_id = self.kwargs["calendar_id"]
        return Event.objects.filter(
            calendar__user=self.request.user, calendar_id=calendar_id
        )
