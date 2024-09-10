from import_export import resources
from .models import Blog, Comment

class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog

class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
