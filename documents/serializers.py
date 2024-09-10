from rest_framework import serializers
from .models import Document
from .models import DocumentClassification
from .models import DocumentTypes


class DocumentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.user_name", read_only=True)

    class Meta:
        model = Document
        fields = "__all__"


class DocumentClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentClassification
        fields = "__all__"


class DocumentTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTypes
        fields = "__all__"
