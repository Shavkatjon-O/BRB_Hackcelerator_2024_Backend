from rest_framework import generics
from .models import Meeting
from .serializers import MeetingSerializer


class MeetingCreateView(generics.CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MeetingListView(generics.ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.filter(user=self.request.user)
