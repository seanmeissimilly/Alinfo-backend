from django.contrib import admin
from .models import Document
from .models import Documentclassification
from .models import Documenttypes
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Document, SimpleHistoryAdmin)
admin.site.register(Documentclassification, SimpleHistoryAdmin)
admin.site.register(Documenttypes, SimpleHistoryAdmin)
