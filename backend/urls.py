from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from django.shortcuts import redirect


# Defino una función para la redirección
def redirect_to_docs(request):
    return redirect("docs/", permanent=True)


urlpatterns = [
    # Establezco las rutas de la API
    path("", redirect_to_docs),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("blogs/", include("blogs.urls")),
    path("applications/", include("applications.urls")),
    path("documents/", include("documents.urls")),
    path("multimedia/", include("multimedia.urls")),
    path("suggestions/", include("suggestions.urls")),
    # Para hacer la documentacion de la Api
    path("docs/", include_docs_urls(title="Alinfo API")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
