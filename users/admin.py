from django.contrib import admin
from .models import User
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(User, SimpleHistoryAdmin)
