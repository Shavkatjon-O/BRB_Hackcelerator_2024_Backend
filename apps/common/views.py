from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View

from .models import Distribution
from .serializers import DistributionSerializer

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny


class DistributionView(RetrieveAPIView):
    serializer_class = DistributionSerializer
    queryset = Distribution.objects.all().first()
    permission_classes = [AllowAny]
