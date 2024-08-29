from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


# Función para la redirección a la documentación
def redirect_to_docs(request):
    return redirect("docs/", permanent=True)


# Rutas principales del proyecto
urlpatterns = [
    # Redirección a la documentación
    path("", redirect_to_docs),
    # Rutas del administrador
    path("admin/", admin.site.urls),
    # Rutas de las aplicaciones
    path("users/", include("users.urls")),
    path("blogs/", include("blogs.urls")),
    path("applications/", include("applications.urls")),
    path("documents/", include("documents.urls")),
    path("multimedia/", include("multimedia.urls")),
    path("suggestions/", include("suggestions.urls")),
    # Rutas para la documentación de la API
    path("docs/schema/", SpectacularAPIView.as_view(), name="docs"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="docs"), name="swagger-ui"),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="docs"), name="redoc"),
]

# Añadir rutas para servir archivos estáticos en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
