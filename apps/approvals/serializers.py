from rest_framework import serializers
from apps.approvals.models import Request


class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = (
            "request_type",
            "description",
            "start_date",
            "end_date",
        )


class RequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = (
            "id",
            "request_type",
            "status",
            "description",
            "start_date",
            "end_date",
        )
