from rest_framework import generics

from apps.approvals.models import Request
from apps.approvals.serializers import RequestCreateSerializer, RequestListSerializer


class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class RequestListAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestListSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
