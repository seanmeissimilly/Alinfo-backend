from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .permissions import IsAdmin, IsEditor, IsReader
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import UserSerializer, UserSerializerWithToken


# todo:Login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializers = UserSerializerWithToken(self.user).data

        for token, user in serializers.items():
            data[token] = user

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# todo:Register
@api_view(["POST"])
def register(request):
    data = request.data

    try:
        user = User.objects.create(
            user_name=data["user_name"],
            email=data["email"],
            password=make_password(data["password"]),
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {"detalles": "Algo salió mal"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


# todo:Update
@api_view(["PUT"])
# !:Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def putUser(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.user_name = data["user_name"]
    user.bio = data["bio"]
    user.email = data["email"]
    user.role = data["role"]
    if data["password"] != "":
        user.password = make_password(data["password"])
    user.save()
    return Response(serializer.data)


# todo:update profile image user
@api_view(["POST"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def uploadImage(request):
    data = request.data
    user_id = data["user_id"]
    user = User.objects.get(id=user_id)
    user.image = request.FILES.get("image")
    user.save()
    return Response("Imagen subida")


# todo:List authenticated user
@api_view(["GET"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# todo:List solo
@api_view(["GET"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getSoloUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# todo:List all
@api_view(["GET"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# todo:Delete
@api_view(["DELETE"])
# !: Reviso si está autentificado y es tiene rol de Admin.
@permission_classes([IsAuthenticated & IsAdmin])
def deleteUser(request, pk):
    user_delete = User.objects.get(id=pk)
    user = request.user
    # !: Reviso que el usuario que hizo la petición tenga el rol de admin.
    if user.role == "admin":
        user_delete.delete()
        return Response("Usuario Eliminado")
    else:
        return Response({"Error": "No autorizado"}, status=status.HTTP_401_UNAUTHORIZED)
