from rest_framework import serializers
from .models import Application, ApplicationClassification


class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.user_name", read_only=True)

    class Meta:
        model = Application
        fields = "__all__"


class ApplicationClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationClassification
        fields = "__all__"
