from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MultimediaclassificationSerializer, MultimediaSerializer
from .models import Multimedia, Multimediaclassification
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from users.permissions import IsAdmin, IsAdminOrIsEditorAndOwner, IsEditor


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class MultimediaView(viewsets.ModelViewSet):
    serializer_class = MultimediaSerializer
    queryset = Multimedia.objects.all()

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
class MultimediaclassificationView(viewsets.ModelViewSet):
    serializer_class = MultimediaclassificationSerializer
    queryset = Multimediaclassification.objects.all()

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            self.permission_classes = [IsAuthenticated, IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
