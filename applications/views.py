from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApplicationSerializer, ApplicationclassificationSerializer
from .models import Application, Applicationclassification
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsAdminOrIsEditorAndOwner, IsEditor
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
import os


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class ApplicationView(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

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


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class ApplicationclassificationView(viewsets.ModelViewSet):
    serializer_class = ApplicationclassificationSerializer
    queryset = Applicationclassification.objects.all()

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            self.permission_classes = [IsAuthenticated, IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
