from django.db import models
from users.models import User


# Modelo de Blog
class Blog(models.Model):
    body = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="blog_picture/",
        default="/blog_picture/noticia.jpg",
    )
    REQUIRED_FIELDS = ["body"]

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.body


# Modelo de Comentario
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ["blog", "text"]

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.text
