from django.db import models
from users.models import User
from simple_history.models import HistoricalRecords
from auditlog.registry import auditlog


# Creo un nomenclador para clasificar lass multimedias.
class Multimediaclassification(models.Model):
    description = models.CharField(max_length=100, unique=True)
    history = HistoricalRecords()

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.description


auditlog.register(Multimediaclassification)


# Modelo de Multimedia
class Multimedia(models.Model):
    title = models.CharField(max_length=200)
    data = models.FileField(upload_to="multimedia/", null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    multimediaclassification = models.ForeignKey(
        Multimediaclassification, on_delete=models.SET_NULL, null=True, blank=True
    )
    history = HistoricalRecords()
    REQUIRED_FIELDS = ["title"]

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.title


auditlog.register(Multimedia)
