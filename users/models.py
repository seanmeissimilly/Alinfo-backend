from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from simple_history.models import HistoricalRecords
from auditlog.registry import auditlog
from django.core.validators import FileExtensionValidator
from django.core.exceptions import PermissionDenied


class CustomAccountManager(BaseUserManager):
    def create_user(self, user_name, email, password, **other_fields):
        if not email:
            raise ValueError(
                _("Debes proporcionar una dirección de correo electrónico")
            )
        # todo: Para que el correo y el usuario sean con letras minúsculas.
        email = self.normalize_email(email)
        user_name = self.normalize_email(user_name)
        user = self.model(user_name=user_name, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_name, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("role", "admin")

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superusuario debe ser asignada a is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superusuario debe ser asignada a is_superuser=True.")
        return self.create_user(user_name, email, password, **other_fields)


# todo: Definir los posibles valores del campo role
ROL_CHOICES = (
    ("admin", "Administrador"),
    ("editor", "Editor"),
    ("reader", "Lector"),
)


# todo: Modelo de Usuario.
class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    bio = models.TextField(_("bio"), max_length=500, blank=True)
    # todo: Foto por defecto de los usuarios al crearse.
    image = models.ImageField(
        null=True,
        blank=True,
        default="profile_picture/Isotipo.png",
        upload_to="profile_picture/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"]
            )
        ],
    )
    is_staff = models.BooleanField(default=False)
    # Para llevar si el usuario está activo.
    is_active = models.BooleanField(default=True)
    # Para los roles, establezco por defecto reader.
    role = models.CharField(max_length=10, choices=ROL_CHOICES, default="reader")
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    history = HistoricalRecords()
    objects = CustomAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    # todo: Función para que no se pueda eliminar a un superusuario.
    def delete(self, *args, **kwargs):
        # todo: Verifica si el usuario que intenta eliminar es un superusuario
        if self.is_superuser:
            raise PermissionDenied(
                "No puedes eliminar a un superusuario. Por favor, contacta con el administrador del sistema si necesitas más ayuda."
            )
        super(User, self).delete(*args, **kwargs)

    # todo: Para que se muestre en el modulo de administración
    def __str__(self):
        return self.user_name


auditlog.register(User)


class Captcha(models.Model):
    text = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.CharField(max_length=200, blank=True, null=True)

    def is_valid(self):
        # Definir el tiempo de validez en minutos (por ejemplo, 5 minutos)
        expiration_time = timezone.now() - timezone.timedelta(minutes=5)
        return self.created_at >= expiration_time
