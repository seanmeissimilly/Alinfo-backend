from rest_framework import serializers
from .models import Suggestion


class SuggestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.user_name", read_only=True)

    class Meta:
        model = Suggestion
        fields = "__all__"
