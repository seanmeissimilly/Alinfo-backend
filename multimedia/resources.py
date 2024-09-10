from import_export import resources
from .models import Multimedia, MultimediaClassification

class MultimediaResource(resources.ModelResource):
    class Meta:
        model = Multimedia

class MultimediaClassificationResource(resources.ModelResource):
    class Meta:
        model = MultimediaClassification
