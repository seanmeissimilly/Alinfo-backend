from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .permissions import IsAdmin
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.exceptions import TokenError
from django.utils.translation import gettext as _


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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
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
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


# todo:Update Solo
@api_view(["PUT"])
# !:Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def putUserSolo(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(
            {"Error": "usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.user_name = data["user_name"]
    user.bio = data["bio"]
    user.email = data["email"]
    user.role = data["role"]
    if data["password"] != "":
        user.password = make_password(data["password"])
    user.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


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
    return Response("Imagen subida", status=status.HTTP_202_ACCEPTED)


# todo:List authenticated user
@api_view(["GET"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


# todo:List solo
@api_view(["GET"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getSoloUser(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(
            {"Error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


# todo:List all
@api_view(["GET"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# todo:Delete
@api_view(["DELETE"])
# !: Reviso si está autentificado y es tiene rol de Admin.
@permission_classes([IsAuthenticated & IsAdmin])
def deleteUser(request, pk):
    try:
        user_delete = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(
            {"Error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    user = request.user
    # !: Reviso que el usuario que hizo la petición tenga el rol de admin.
    if user.role == "admin":
        user_delete.delete()
        return Response("Usuario Eliminado", status=status.HTTP_200_OK)
    else:
        return Response({"Error": "No autorizado"}, status=status.HTTP_401_UNAUTHORIZED)


# # todo:Logout
# class BlacklistRefreshView(APIView):
#     def post(self, request):
#         token = RefreshToken(request.data.get("refresh"))
#         token.blacklist()
#         return Response("Éxito", status=status.HTTP_200_OK)
