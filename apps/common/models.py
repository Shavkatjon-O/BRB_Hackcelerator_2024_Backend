from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class DesktopDownload(BaseModel):
    file = models.FileField(upload_to="desktop_downloads/")


class MobileDownload(BaseModel):
    file = models.FileField(upload_to="mobile_downloads/")


from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import generics


class DesktopDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesktopDownload
        fields = ["file"]


class MobileDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileDownload
        fields = ["file"]


class DesktopDownloadDetailView(generics.ListAPIView):
    queryset = DesktopDownload.objects.all().order_by("-created_at")[:1]
    serializer_class = DesktopDownloadSerializer
    permission_classes = [AllowAny]


class MobileDownloadDetailView(generics.ListAPIView):
    queryset = MobileDownload.objects.all().order_by("-created_at")[:1]
    serializer_class = MobileDownloadSerializer
    permission_classes = [AllowAny]
