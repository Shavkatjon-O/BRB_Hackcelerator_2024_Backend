from rest_framework import generics

from django.contrib.auth import get_user_model
from apps.users.serializers import SignupSerializer

User = get_user_model()


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):

        print(request.data)

        print(request.data.get("email"))
        print(request.data.get("password"))

        return self.create(request, *args, **kwargs)
