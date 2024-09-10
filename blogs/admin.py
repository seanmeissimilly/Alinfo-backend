from django.contrib import admin
from .models import Blog, Comment
from simple_history.admin import SimpleHistoryAdmin
from .resources import BlogResource, CommentResource
from import_export.admin import ImportExportModelAdmin

@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = BlogResource

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = CommentResource    


