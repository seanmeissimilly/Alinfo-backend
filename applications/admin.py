from django.contrib import admin
from .models import Application, ApplicationClassification
from simple_history.admin import SimpleHistoryAdmin
from .resources import ApplicationResource, ApplicationClassificationResource
from import_export.admin import ImportExportModelAdmin

@admin.register(Application)
class ApplicationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = ApplicationResource

@admin.register(ApplicationClassification)
class ApplicationClassificationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = ApplicationClassificationResource