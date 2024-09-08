from django.contrib import admin
from .models import Blog
from .models import Comment
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Blog, SimpleHistoryAdmin)
admin.site.register(Comment, SimpleHistoryAdmin)
