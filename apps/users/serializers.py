from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                email=validated_data["email"], password=validated_data["password"]
            )
            return user
        except Exception as e:
            raise serializers.ValidationError(str(e))


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "date_of_birth",
            "address",
            "job_title",
            "department",
            "education",
            "employment_start_date",
            "skills",
        )
