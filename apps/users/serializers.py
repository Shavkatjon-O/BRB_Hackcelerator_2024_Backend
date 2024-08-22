from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                email=validated_data["email"], password=validated_data["password"]
            )
            return user
        except Exception as e:
            raise serializers.ValidationError(str(e))
