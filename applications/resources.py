from import_export import resources
from .models import Application, ApplicationClassification

class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application

class ApplicationClassificationResource(resources.ModelResource):
    class Meta:
        model = ApplicationClassification
