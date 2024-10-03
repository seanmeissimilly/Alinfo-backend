import random
import string
import uuid
import logging
import os
from django.http import JsonResponse
from captcha.image import ImageCaptcha
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from users.models import Captcha
from django.conf import settings
from django.utils import timezone


def generate_captcha_text(length=4):
    letters = string.ascii_uppercase + string.digits
    return "".join(random.choice(letters) for i in range(length))


def get_file_path(file_name):
    return os.path.join(settings.MEDIA_ROOT, f"captchas/{file_name}").replace("\\", "/")


def delete_file(file_path):
    if default_storage.exists(file_path):
        default_storage.delete(file_path)


class CaptchaImageView(APIView):
    def get(self, request, *args, **kwargs):
        image = ImageCaptcha()
        captcha_text = generate_captcha_text()
        data = image.generate(captcha_text)

        # Generar un nombre de archivo aleatorio
        file_name = f"{uuid.uuid4()}.png"
        file_path = f"captchas/{file_name}"
        default_storage.save(file_path, ContentFile(data.read()))

        # Guardar el CAPTCHA en la base de datos
        Captcha.objects.create(text=captcha_text, image_file=file_name)

        # Devolver la URL de la imagen
        captcha_image_url = default_storage.url(file_path)

        return JsonResponse(
            {"captcha_image_url": captcha_image_url},
        )


def verify_captcha(captcha_value):
    try:
        # todo: Eliminar CAPTCHAs expirados y sus archivos de imagen
        expiration_time = timezone.now() - timezone.timedelta(minutes=3)
        expired_captchas = Captcha.objects.filter(created_at__lt=expiration_time)

        for captcha in expired_captchas:
            file_path = get_file_path(captcha.image_file)
            delete_file(file_path)

        expired_captchas.delete()  # todo: Eliminar los CAPTCHAs expirados de la base de datos

        captcha = Captcha.objects.filter(text=captcha_value.upper()).first()
        if captcha and captcha.is_valid():
            file_path = get_file_path(captcha.image_file)
            delete_file(file_path)

            captcha.delete()  # todo: Eliminar el CAPTCHA de la base de datos
            return True
        return False
    except Exception:
        return
