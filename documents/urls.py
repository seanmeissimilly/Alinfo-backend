from django.urls import path
from documents import views
from django.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"", views.DocumentView, "documents")
router.register(r"types", views.DocumenttypesView, "documentstypes")
router.register(
    r"classification", views.DocumentclassificationView, "documentsclassification"
)

urlpatterns = [
    path("", include(router.urls)),
]
