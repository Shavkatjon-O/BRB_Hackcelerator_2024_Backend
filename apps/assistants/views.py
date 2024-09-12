from django.shortcuts import render

# Create your views here.


from .chain import get_chain
from rest_framework.generics import CreateAPIView

from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import ChatSerializer


class ChatView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ChatSerializer

    def post(self, request, *args, **kwargs):
        chain = get_chain()

        question = request.data.get("question")
        response = chain.invoke(question)

        return Response(response)
