from rest_framework import generics

from django.contrib.auth import get_user_model
from apps.users.serializers import SignupSerializer

User = get_user_model()


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
