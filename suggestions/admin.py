from django.contrib import admin
from .models import Suggestion
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Suggestion, SimpleHistoryAdmin)
