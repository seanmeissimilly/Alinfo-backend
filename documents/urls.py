from django.urls import path, include
from documents import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"doc", views.DocumentView, basename="document")
router.register(r"types", views.DocumentTypesView, basename="documentTypes")
router.register(
    r"classification",
    views.DocumentClassificationView,
    basename="documentClassification",
)


urlpatterns = [
    path("", include(router.urls)),
    path("search/", views.DocumentSearchView.as_view(), name="documentsearch"),
]
