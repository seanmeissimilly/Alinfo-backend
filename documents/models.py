from django.db import models
from users.models import User
from simple_history.models import HistoricalRecords
from auditlog.registry import auditlog
from django.core.validators import FileExtensionValidator
from tika import parser


def extract_text(file_path):
    parsed = parser.from_file(file_path)
    return parsed["content"]


# Creo un nomenclador para clasificar los documentos.
class DocumentClassification(models.Model):
    description = models.CharField(max_length=100, unique=True)
    history = HistoricalRecords()

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.description


auditlog.register(DocumentClassification)


# Creo un nomenclador para tipos de documentos.
class DocumentTypes(models.Model):
    description = models.CharField(max_length=100, unique=True)
    history = HistoricalRecords()

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.description


auditlog.register(DocumentTypes)


# Modelo de Documentos
class Document(models.Model):
    title = models.CharField(max_length=200)
    author = models.TextField(max_length=200, blank=True)
    data = models.FileField(
        upload_to="documents/",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "pdf",
                    "doc",
                    "docx",
                    "xls",
                    "xlsx",
                    "txt",
                    "tex",
                    "odt",
                    "ods",
                    "odp",
                ]
            )
        ],
    )
    description = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    documentclassification = models.ForeignKey(
        DocumentClassification, on_delete=models.SET_NULL, null=True, blank=True
    )
    documenttypes = models.ForeignKey(
        DocumentTypes, on_delete=models.SET_NULL, null=True, blank=True
    )
    history = HistoricalRecords()
    extracted_text = models.TextField(blank=True, null=True)
    REQUIRED_FIELDS = ["title"]

    def save(self, *args, **kwargs):
        if self.data:
            self.extracted_text = extract_text(self.data.path)
        super().save(*args, **kwargs)

    # Para que se muestre en el modulo de administración
    def __str__(self):
        return self.title


auditlog.register(Document)
