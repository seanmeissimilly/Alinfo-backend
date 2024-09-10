from django.urls import path, include
from documents import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"doc", views.DocumentView)
router.register(r"types", views.DocumentTypesView)
router.register(r"classification", views.DocumentClassificationView)

urlpatterns = [
    path("", include(router.urls)),
]
