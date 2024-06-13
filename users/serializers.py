from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "user_name",
            "email",
            "role",
            "is_admin",
            "bio",
            "first_name",
            "image",
            "start_date",
        ]

    # def __init__(self, *args, **kwargs):
    #     super(UserSerializer, self).__init__(*args, **kwargs)
    #     self.fields["user_name"].required = True
    #     self.fields["email"].required = True
    #     self.fields["password"].required = True

    def get_is_admin(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "user_name",
            "email",
            "role",
            "is_admin",
            "bio",
            "first_name",
            "image",
            "start_date",
            "token",
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
