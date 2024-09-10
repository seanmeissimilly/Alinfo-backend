from django.contrib import admin
from .models import Suggestion
from simple_history.admin import SimpleHistoryAdmin
from .resources import SuggestionResource
from import_export.admin import ImportExportModelAdmin

@admin.register(Suggestion)
class SuggestionAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = SuggestionResource
