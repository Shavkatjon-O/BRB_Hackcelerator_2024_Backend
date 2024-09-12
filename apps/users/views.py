from rest_framework import generics
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model
from apps.users import serializers

from apps.users.models import UserTypeChoices

from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


class SignUpView(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    queryset = User.objects.all()
    serializer_class = serializers.SignUpSerializer


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.UserProfileSerializer

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.UserProfileUpdateSerializer

    def get_object(self):
        return self.request.user


class ToggleUserTypeView(generics.GenericAPIView):
    def post(self, request):
        current_user = request.user
        current_user_type = current_user.user_type

        if current_user_type == UserTypeChoices.LOAN_MANAGER:
            current_user.user_type = UserTypeChoices.BANK_TELLER

        elif current_user_type == UserTypeChoices.BANK_TELLER:
            current_user.user_type = UserTypeChoices.LOAN_MANAGER

        current_user.save()

        return Response(
            {
                "message": "User type updated successfully",
                "new_user_type": current_user.user_type,
            },
            status=status.HTTP_200_OK,
        )
