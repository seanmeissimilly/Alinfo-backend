from django.urls import path
from documents import views
from django.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"", views.DocumentView, "documents")

urlpatterns = [
    path("", include(router.urls)),
    path("types/", views.getDocumentTypes),
    path("classification/", views.getDocumentClassification),
]
