from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(
                _("Debes proporcionar una dirección de correo electrónico")
            )
        email = self.normalize_email(email)
        user = self.model(
            email=email, user_name=user_name, first_name=first_name, **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("role", "admin")

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superusuario debe ser asignada a is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superusuario debe ser asignada a is_superuser=True.")
        return self.create_user(email, user_name, first_name, password, **other_fields)


# Definir los posibles valores del campo role
ROL_CHOICES = (
    ("admin", "Administrador"),
    ("editor", "Editor"),
    ("reader", "Lector"),
)


# Modelo de Usuario.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    bio = models.TextField(_("bio"), max_length=500, blank=True)
    # Foto por defecto de los usuarios al crearse.
    image = models.ImageField(
        null=True, blank=True, default="/profile_picture/Isotipo.png"
    )
    is_staff = models.BooleanField(default=False)
    # Para llevar si el usuario está activo.
    is_active = models.BooleanField(default=True)
    # Para los roles, establezco por defecto reader.
    role = models.CharField(max_length=10, choices=ROL_CHOICES, default="reader")
    objects = CustomAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "first_name"]

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.user_name
