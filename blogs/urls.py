from django.urls import path
from . import views


urlpatterns = [
    # Rutas de la aplicación Blog
    path("get/", views.getBlogs),
    path("get/<int:pk>/", views.getSoloBlog),
    path("post/", views.postBlog),
    path("put/<int:pk>/", views.putBlog),
    path("delete/<int:pk>/", views.deleteBlog),
    path("comment/<int:pk>/", views.comment),
    path("image/<int:pk>/", views.uploadImage),
]
