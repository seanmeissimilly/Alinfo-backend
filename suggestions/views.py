from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SuggestionSerializer
from .models import Suggestion
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from users.permissions import IsAdmin, IsEditor, IsReader


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class SuggestionView(viewsets.ModelViewSet):
    serializer_class = SuggestionSerializer
    queryset = Suggestion.objects.all()
