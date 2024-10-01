from django.http import HttpResponse
from captcha.image import ImageCaptcha
import random
import string


def generate_captcha_text(length=4):
    letters = string.ascii_uppercase + string.digits
    return "".join(random.choice(letters) for i in range(length))


def captcha_image(request):
    image = ImageCaptcha()
    captcha_text = generate_captcha_text()
    request.session["captcha_text"] = captcha_text  # Almacenar el CAPTCHA en la sesión
    data = image.generate(captcha_text)
    return HttpResponse(data, content_type="image/png")


def verify_captcha(request):
    user_input = request.POST.get("captcha")
    captcha_text = request.session.get("captcha_text")
    return user_input and user_input.upper() == captcha_text
