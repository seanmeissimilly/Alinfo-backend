from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"comment", views.CommentView)

urlpatterns = [
    # Rutas de la aplicación Blog
    path("get/", views.getBlogs),
    path("get/<int:pk>/", views.getSoloBlog),
    path("post/", views.postBlog),
    path("put/<int:pk>/", views.putBlog),
    path("delete/<int:pk>/", views.deleteBlog),
    path("image/<int:pk>/", views.uploadImage),
    # Rutas de Comentario.
    path("", include(router.urls)),
]
