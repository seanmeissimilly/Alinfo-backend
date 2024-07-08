from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DocumentclassificationSerializer
from .serializers import DocumenttypesSerializer
from .serializers import DocumentSerializer
from .models import Document
from .models import Documentclassification
from .models import Documenttypes
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsEditor, IsReader


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated & IsAdmin])
class DocumenttypesView(viewsets.ModelViewSet):
    serializer_class = DocumenttypesSerializer
    queryset = Documenttypes.objects.all()


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated & IsAdmin])
class DocumentclassificationView(viewsets.ModelViewSet):
    serializer_class = DocumentclassificationSerializer
    queryset = Documentclassification.objects.all()


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
