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
        fields = "__all__"


class MobileDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileDownload
        fields = "__all__"


class DesktopDownloadDetailView(generics.RetrieveAPIView):
    queryset = DesktopDownload.objects.all().first()
    serializer_class = DesktopDownloadSerializer
    permission_classes = [AllowAny]


class MobileDownloadDetailView(generics.RetrieveAPIView):
    queryset = MobileDownload.objects.all().first()
    serializer_class = MobileDownloadSerializer
    permission_classes = [AllowAny]
