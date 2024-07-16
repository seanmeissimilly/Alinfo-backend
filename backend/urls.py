from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from rest_framework import permissions


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Alinfo API",
#         default_version="v1.0.0",
#         description="Bienvenido a la documentación de la API Alinfo",
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
    # Establezco las rutas de la API
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("blogs/", include("blogs.urls")),
    path("applications/", include("applications.urls")),
    path("documents/", include("documents.urls")),
    path("multimedia/", include("multimedia.urls")),
    path("suggestions/", include("suggestions.urls")),
    # Para hacer la documentacion de la Api
    path("docs/", include_docs_urls(title="Alinfo API")),
    # path(
    #     "docs/swagger/",
    #     schema_view.with_ui("swagger", cache_timeout=0),
    #     name="schema-swagger-ui",
    # ),
    # path(
    #     "docs/redoc/",
    #     schema_view.with_ui("redoc", cache_timeout=0),
    #     name="schema-redoc",
    # ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
