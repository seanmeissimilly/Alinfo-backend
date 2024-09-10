from django.contrib import admin
from .models import Document
from .models import DocumentClassification
from .models import DocumentTypes
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import DocumentResource, DocumentTypesResource, DocumentClassificationResource
from import_export.admin import ImportExportModelAdmin

@admin.register(Document)
class DocumentAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = DocumentResource

@admin.register(DocumentClassification)
class DocumentClassificationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = DocumentClassificationResource

@admin.register(DocumentTypes)
class DocumentTypesAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = DocumentTypesResource

