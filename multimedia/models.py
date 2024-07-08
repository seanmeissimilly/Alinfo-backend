from django.db import models
from users.models import User


# Creo un nomenclador para clasificar lass multimedias.
class Multimediaclassification(models.Model):
    description = models.CharField(max_length=50, unique=True)

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.description


# Modelo de Multimedia
class Multimedia(models.Model):
    name = models.CharField(max_length=100)
    data = models.FileField(upload_to="multimedia/", null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    multimediaclassification = models.ForeignKey(
        Multimediaclassification, on_delete=models.SET_NULL, null=True, blank=True
    )
    REQUIRED_FIELDS = ["name", "user"]

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.name
