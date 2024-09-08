from django.db import models
from users.models import User
from simple_history.models import HistoricalRecords
from auditlog.registry import auditlog


# Modelo de Blog
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="blog_picture/",
        default="blog_picture/noticia.jpg",
    )
    history = HistoricalRecords()
    REQUIRED_FIELDS = ["title", "body"]

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.title


auditlog.register(Blog)


# Modelo de Comentario
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()
    REQUIRED_FIELDS = ["blog", "text"]

    # Para que se muestre en el modulo de administración
    def __str__(self):
        formatted_date = self.date.strftime("%d/%m/%Y")
        return f"Comentario por {self.user.user_name} el {formatted_date}"


auditlog.register(Comment)
