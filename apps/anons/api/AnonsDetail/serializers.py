from rest_framework import serializers
from apps.anons.models import Anons


class AnonsDetailSerializer(serializers.ModelSerializer):
    is_read = serializers.SerializerMethodField()

    class Meta:
        model = Anons
        fields = (
            "id",
            "title",
            "description",
            "created_at",
        )

    def get_is_read(self, obj):
        return obj.read_by.filter(id=self.context["request"].user.id).exists()


__all__ = ("AnonsDetailSerializer",)
