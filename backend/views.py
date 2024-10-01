import random
import string
import os
from django.http import JsonResponse
from captcha.image import ImageCaptcha
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def generate_captcha_text(length=4):
    letters = string.ascii_uppercase + string.digits
    return "".join(random.choice(letters) for i in range(length))


class CaptchaImageView(APIView):
    def get(self, request, *args, **kwargs):
        image = ImageCaptcha()
        captcha_text = generate_captcha_text()
        print(captcha_text)
        data = image.generate(captcha_text)

        # Guardar la imagen en un archivo temporal
        file_path = os.path.join(settings.MEDIA_ROOT, f"{captcha_text}.png")
        default_storage.save(file_path, ContentFile(data.read()))

        # Crear un token con el texto del CAPTCHA sin asociarlo a un usuario
        token = AccessToken()
        token["captcha_text"] = captcha_text
        captcha_token = str(token)

        # Devolver la URL de la imagen
        captcha_image_url = default_storage.url(file_path)

        return JsonResponse(
            {"captcha_image_url": captcha_image_url, "captcha_token": captcha_token},
        )


def verify_captcha(captcha_token, user_input):
    try:
        token = AccessToken(captcha_token)
        captcha_text = token["captcha_text"]
        return user_input and user_input.upper() == captcha_text
    except Exception:
        return False
