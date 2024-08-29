from rest_framework import serializers
from apps.events.models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "start_date",
            "end_date",
        )


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "start_date",
            "end_date",
        )


class EventCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "title",
            "description",
            "start_date",
            "end_date",
        )
