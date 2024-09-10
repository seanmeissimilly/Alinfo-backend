from rest_framework import serializers
from .models import Multimedia
from .models import MultimediaClassification


class MultimediaSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.user_name", read_only=True)

    class Meta:
        model = Multimedia
        fields = "__all__"


class MultimediaClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaClassification
        fields = "__all__"
