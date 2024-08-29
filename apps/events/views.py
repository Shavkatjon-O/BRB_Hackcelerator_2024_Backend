from rest_framework import generics
from apps.events import serializers, models


class EventListRetrieveView(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventListSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class EventCreateView(generics.CreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventRetrieveView(generics.RetrieveAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventDetailSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class EventUpdateView(generics.UpdateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventCreateUpdateSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class EventDestroyView(generics.DestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventDetailSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
