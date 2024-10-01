from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .permissions import IsAdmin
from .serializers import UserSerializer, UserSerializerWithToken
from django.utils.translation import gettext as _
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiRequest,
)
from backend.views import verify_captcha


# todo:Login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializers = UserSerializerWithToken(self.user).data

        for token, user in serializers.items():
            data[token] = user

        # Capturar la IP del usuario
        request = self.context.get("request")
        if request:
            ip = request.META.get("REMOTE_ADDR")
            self.user.last_login_ip = ip
            self.user.save()

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # Verificar CAPTCHA
        captcha_response = verify_captcha(request)
        if not captcha_response:
            return Response(
                {"error": "Invalid CAPTCHA"}, status=status.HTTP_400_BAD_REQUEST
            )

        return super().post(request, *args, **kwargs)


# todo : Función para chequear que un username o un correo ya están tomados.
def check_user_exists(data):
    if User.objects.filter(email=data["email"]).exists():
        return {
            "error": _("Ya existe una cuenta con este correo electrónico.")
        }, status.HTTP_409_CONFLICT
    if User.objects.filter(user_name=data["user_name"]).exists():
        return {
            "error": _("Ya existe una cuenta con este nombre de usuario.")
        }, status.HTTP_409_CONFLICT
    return None, None


# todo:Register
@api_view(["POST"])
def register(request):

    # Verificar CAPTCHA
    captcha_response = verify_captcha(request)
    if not captcha_response:
        return Response(
            {"error": "Invalid CAPTCHA"}, status=status.HTTP_400_BAD_REQUEST
        )

    data = request.data
    try:
        error_message, error_status = check_user_exists(data)
        if error_message:
            return Response(error_message, status=error_status)

        user_ip = request.META.get("HTTP_X_FORWARDED_FOR")
        if user_ip:
            user_ip = user_ip.split(",")[0]
        else:
            user_ip = request.META.get("REMOTE_ADDR")

        user = User.objects.create(
            user_name=data["user_name"],
            email=data["email"],
            password=make_password(data["password"]),
            last_login_ip=user_ip,
        )
        # todo: Verificar si hay una imagen en los datos
        if "image" in request.FILES:
            user.image = request.FILES["image"]
            user.save()

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        message = {"error": _("Algo salió mal: ") + str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


# todo:Update
@api_view(["PUT"])
# !:Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def putUser(request):
    user = request.user
    data = request.data
    try:
        user.user_name = data["user_name"]
        user.bio = data["bio"]
        user.email = data["email"]
        user.role = data["role"]
        if data["password"]:
            user.password = make_password(data["password"])
        # todo: Verificar si hay una imagen en los datos
        if "image" in request.FILES:
            user.image = request.FILES["image"]
        user.save()
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        message = {"error": _("Algo salió mal: ") + str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


# todo:Update Solo
@api_view(["PUT"])
# !:Reviso si está autentificado.
@permission_classes([IsAuthenticated & IsAdmin])
def putUserSolo(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(
            {"error": _("Usuario no encontrado")}, status=status.HTTP_404_NOT_FOUND
        )

    data = request.data
    try:

        user.user_name = data["user_name"]
        user.bio = data["bio"]
        user.email = data["email"]
        user.role = data["role"]
        if data["password"]:
            user.password = make_password(data["password"])
        user.save()
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        message = {"error": _("Algo salió mal: ") + str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


# todo: update profile image user
@api_view(["POST"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def uploadImage(request):
    data = request.data
    user_id = data["user_id"]

    # todo: Busco el usuario según el id.
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(
            {"error": _("Usuario no encontrado")}, status=status.HTTP_404_NOT_FOUND
        )

    user.image = request.FILES.get("image")
    user.save()
    return Response("Imagen subida", status=status.HTTP_202_ACCEPTED)


# todo:List authenticated user
@api_view(["GET"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
@extend_schema(
    operation_id="user_profile",
    summary="Obtener perfil del usuario autenticado",
    description="Este endpoint permite obtener el perfil del usuario autenticado.",
    responses={
        200: OpenApiResponse(description="Perfil del usuario autenticado"),
        400: OpenApiResponse(description="Error en la solicitud"),
    },
)
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
            {"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


# todo:List all
@api_view(["GET"])
@extend_schema(
    operation_id="list_users",
    summary="Listar todos los usuarios",
    description="Este endpoint permite listar todos los usuarios.",
    responses={
        200: OpenApiResponse(description="Lista de usuarios"),
        400: OpenApiResponse(description="Error en la solicitud"),
    },
)
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
@extend_schema(
    operation_id="delete_user",
    summary="Eliminar un usuario",
    description="Este endpoint permite eliminar un usuario.",
    parameters=[
        OpenApiParameter(
            name="pk", type=int, description="ID del usuario a eliminar", required=True
        )
    ],
    responses={
        200: OpenApiResponse(description="Usuario eliminado exitosamente"),
        401: OpenApiResponse(description="No autorizado"),
        404: OpenApiResponse(description="Usuario no encontrado"),
        400: OpenApiResponse(description="Error en la solicitud"),
    },
)
def deleteUser(request, pk):
    try:
        user_delete = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(
            {"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    user = request.user
    # !: Reviso que el usuario que hizo la petición tenga el rol de admin.
    if user.role == "admin":
        user_delete.delete()
        return Response("Usuario Eliminado", status=status.HTTP_200_OK)
    else:
        return Response({"error": "No autorizado"}, status=status.HTTP_401_UNAUTHORIZED)


# todo:Logout
class LogoutView(APIView):
    @extend_schema(
        operation_id="user_logout",
        summary="Logout del usuario",
        description="Este endpoint permite a un usuario cerrar sesión invalidando su token de refresco.",
        request=OpenApiRequest(
            {
                "application/json": {
                    "type": "object",
                    "properties": {
                        "refresh": {
                            "type": "string",
                            "description": "Token de refresco",
                            "example": "tu_refresh_token_aqui",
                        }
                    },
                    "required": ["refresh"],
                }
            }
        ),
        responses={
            205: OpenApiResponse(description="Logout exitoso"),
            400: OpenApiResponse(description="Error en la solicitud"),
        },
    )
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error": "Token de refresco no proporcionado"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"data": _("Logout exitoso")},
                status=status.HTTP_205_RESET_CONTENT,
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
