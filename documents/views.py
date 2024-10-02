from django.shortcuts import render
from rest_framework import viewsets, status, generics
from .serializers import (
    DocumentClassificationSerializer,
    DocumentTypesSerializer,
    DocumentSerializer,
)
from .models import Document, DocumentClassification, DocumentTypes
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsEditor, IsAdminOrIsEditorAndOwner
from django.utils.translation import gettext as _
from rest_framework.response import Response
import os


class DocumentTypesView(viewsets.ModelViewSet):
    serializer_class = DocumentTypesSerializer
    queryset = DocumentTypes.objects.all()

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            self.permission_classes = [IsAuthenticated, IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class DocumentClassificationView(viewsets.ModelViewSet):
    serializer_class = DocumentClassificationSerializer
    queryset = DocumentClassification.objects.all()

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            self.permission_classes = [IsAuthenticated, IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def perform_create(self, serializer):
        # Asignar el usuario autenticado al campo 'user'
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated, IsAdmin | IsEditor]
        elif self.request.method in ["PUT", "DELETE"]:
            self.permission_classes = [IsAuthenticated, IsAdminOrIsEditorAndOwner]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = instance.data.path
        response = super().destroy(request, *args, **kwargs)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                message = {
                    "error": _("Algo salió mal al eliminar el archivo: ") + str(e)
                }
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        return response


class DocumentSearchView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_queryset(self):
        query = self.request.query_params.get("q", None)
        if query:
            return Document.objects.filter(extracted_text__icontains=query)
        return Document.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
