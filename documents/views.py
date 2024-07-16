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
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


@api_view(["GET"])
#!: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getDocumentTypes(request):
    type = Documenttypes.objects.all()
    serializer = Documenttypes(type, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
#!: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getDocumentClassification(request):
    classification = Documentclassification.objects.all()
    serializer = Documentclassification(classification, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
