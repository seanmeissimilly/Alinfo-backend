from django.urls import path, include
from . import views
from rest_framework import routers
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogImageView,
)

router = routers.DefaultRouter()
router.register(r"comment", views.CommentView)

urlpatterns = [
    # Rutas de la aplicación Blog
    path("get/", BlogListView.as_view(), name="get_blogs"),
    path("get/<int:pk>/", BlogDetailView.as_view(), name="get_solo_blog"),
    path("post/", BlogCreateView.as_view(), name="post_blog"),
    path("put/<int:pk>/", BlogUpdateView.as_view(), name="put_blog"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="delete_blog"),
    path("image/<int:pk>/", BlogImageView.as_view(), name="upload_image"),
    # Rutas de Comentario.
    path("", include(router.urls)),
]
