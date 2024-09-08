from django.db import models
from users.models import User
from simple_history.models import HistoricalRecords
from auditlog.registry import auditlog


# Modelo de Sugerancias
class Suggestion(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    history = HistoricalRecords()
    REQUIRED_FIELDS = ["body", "title"]

    # Para que se muestre en el modulo de administración
    def __str__(self):
        formatted_date = self.date.strftime("%d/%m/%Y")
        return f"Sugerencia por {self.user.user_name} el {formatted_date}"


auditlog.register(Suggestion)
