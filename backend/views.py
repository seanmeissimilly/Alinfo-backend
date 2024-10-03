import random
import string
import uuid
import os
from django.http import JsonResponse
from captcha.image import ImageCaptcha
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from users.models import Captcha
from django.conf import settings


def generate_captcha_text(length=4):
    letters = string.ascii_uppercase + string.digits
    return "".join(random.choice(letters) for i in range(length))


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
        Captcha.objects.create(text=captcha_text)

        # Devolver la URL de la imagen
        captcha_image_url = default_storage.url(file_path)

        return JsonResponse(
            {"captcha_image_url": captcha_image_url},
        )


def verify_captcha(captcha_value):
    try:
        captcha = Captcha.objects.filter(text=captcha_value.upper()).first()
        if captcha and captcha.is_valid():
            # Obtener la ruta del archivo de imagen
            file_name = f"captchas/{captcha.text}.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)

            # Eliminar el archivo de imagen si existe
            if default_storage.exists(file_path):
                default_storage.delete(file_path)

            captcha.delete()  # Eliminar el CAPTCHA de la base de datos
            return True
        return False
    except Exception as e:
        return
