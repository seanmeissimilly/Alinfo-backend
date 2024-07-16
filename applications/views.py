from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApplicationSerializer, ApplicationclassificationSerializer
from .models import Application, Applicationclassification
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsAdminOrIsEditorAndOwner, IsEditor


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class ApplicationView(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated, IsAdmin | IsEditor]
        elif self.request.method in ["PUT", "DELETE"]:
            self.permission_classes = [IsAuthenticated, IsAdminOrIsEditorAndOwner]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


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
