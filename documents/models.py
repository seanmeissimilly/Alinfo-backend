from django.db import models
from users.models import User


# Creo un nomenclador para clasificar los documentos.
class Documentclassification(models.Model):
    description = models.CharField(max_length=50, unique=True)

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.description


# Creo un nomenclador para tipos de documentos.
class Documenttypes(models.Model):
    description = models.CharField(max_length=50, unique=True)

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.description


# Modelo de Documentos
class Document(models.Model):
    name = models.CharField(max_length=100)
    data = models.FileField(upload_to="documents/", null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    documentclassification = models.ForeignKey(
        Documentclassification, on_delete=models.SET_NULL, null=True, blank=True
    )
    documenttypes = models.ForeignKey(
        Documenttypes, on_delete=models.SET_NULL, null=True, blank=True
    )
    REQUIRED_FIELDS = ["name"]

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.name
