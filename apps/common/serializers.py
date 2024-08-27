from rest_framework.serializers import ModelSerializer
from apps.common.models import Distribution


class DistributionSerializer(ModelSerializer):
    class Meta:
        model = Distribution
        fields = ("desktop_exe",)
