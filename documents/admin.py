from django.contrib import admin
from .models import Document
from .models import Documentclassification
from .models import Documenttypes

admin.site.register(Document)
admin.site.register(Documentclassification)
admin.site.register(Documenttypes)
