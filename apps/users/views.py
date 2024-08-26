from rest_framework import generics
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model
from apps.users import serializers

User = get_user_model()


class SignUpView(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    queryset = User.objects.all()
    serializer_class = serializers.SignUpSerializer


class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserProfileSerializer

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserProfileUpdateSerializer
