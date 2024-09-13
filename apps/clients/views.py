from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from .serializers import DocumentSerializer
from .models import Document


class DocumentGetAPIView(RetrieveAPIView):
    queryset = Document.objects.all()
    permission_classes = [AllowAny]
    serializer_class = DocumentSerializer
