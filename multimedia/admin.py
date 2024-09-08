from django.contrib import admin
from .models import Multimediaclassification
from .models import Multimedia
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Multimedia, SimpleHistoryAdmin)
admin.site.register(Multimediaclassification, SimpleHistoryAdmin)
