from django.contrib import admin
from .models import User, Captcha
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


@admin.register(Captcha)
class CaptchaAdmin(admin.ModelAdmin):
    list_display = ("text", "created_at", "image_file")
    search_fields = ("text",)
