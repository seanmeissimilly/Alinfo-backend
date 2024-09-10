from django.urls import path
from applications import views
from django.urls import include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"app", views.ApplicationView)
router.register(r"classification", views.ApplicationClassificationView)

urlpatterns = [
    path("", include(router.urls)),
]
