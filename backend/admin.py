from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


class MyModelAdmin(admin.ModelAdmin):
    change_list_template = "admin/myapp/mymodel/change_list.html"

    def changelist_view(self, request, extra_context=None):
        extra_context = {"backup_url": reverse("backup_database")}
        return super().changelist_view(request, extra_context=extra_context)


# admin.site.register(MyModel, MyModelAdmin)
