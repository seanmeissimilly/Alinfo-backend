from django.contrib import admin
from .models import Application, Applicationclassification
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Application, SimpleHistoryAdmin)
admin.site.register(Applicationclassification, SimpleHistoryAdmin)
