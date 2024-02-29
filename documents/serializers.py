from rest_framework import serializers
from .models import Document
from .models import Documentclassification
from .models import Documenttypes


class DocumentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.user_name", read_only=True)

    class Meta:
        model = Document
        fields = "__all__"


class DocumentclassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentclassification
        fields = "__all__"


class DocumenttypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documenttypes
        fields = "__all__"
