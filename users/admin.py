from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import User
from simple_history.admin import SimpleHistoryAdmin
from .resources import UserResource
from import_export.admin import ImportExportModelAdmin


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = UserResource

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.is_superuser and request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)
