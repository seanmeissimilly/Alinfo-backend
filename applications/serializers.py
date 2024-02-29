from rest_framework import serializers
from .models import Application, Applicationclassification


class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.user_name", read_only=True)

    class Meta:
        model = Application
        fields = "__all__"


class ApplicationclassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicationclassification
        fields = "__all__"
