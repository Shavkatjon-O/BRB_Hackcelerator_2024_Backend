from rest_framework import serializers
from apps.applications.models import Application


class ApplicationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


__all__ = ("ApplicationsListSerializer",)
