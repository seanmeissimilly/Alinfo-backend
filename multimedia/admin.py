from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Multimedia, MultimediaClassification
from .resources import MultimediaResource, MultimediaClassificationResource
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Multimedia)
class MultimediaAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = MultimediaResource

@admin.register(MultimediaClassification)
class MultimediaClassificationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = MultimediaClassificationResource

