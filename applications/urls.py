from django.urls import path
from applications import views
from django.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"", views.ApplicationView)
router.register(r"classification", views.ApplicationclassificationView)

urlpatterns = [
    path("", include(router.urls)),
]
