from django.contrib import admin
from .models import User
from simple_history.admin import SimpleHistoryAdmin
from .resources import UserResource
from import_export.admin import ImportExportModelAdmin

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = UserResource
