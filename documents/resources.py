from import_export import resources
from .models import Document,DocumentClassification,DocumentTypes

class DocumentResource(resources.ModelResource):
    class Meta:
        model = Document

class DocumentTypesResource(resources.ModelResource):
    class Meta:
        model = DocumentTypes

class DocumentClassificationResource(resources.ModelResource):
    class Meta:
        model = DocumentClassification       
