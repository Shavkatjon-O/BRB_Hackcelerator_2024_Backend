from rest_framework import generics
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model
from apps.users.serializers import SignupSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


class SignupView(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    queryset = User.objects.all()
    serializer_class = SignupSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            print("Validation Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
