from django.urls import path
from multimedia import views
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"mmt", views.MultimediaView)
router.register(r"classification", views.MultimediaClassificationView)

urlpatterns = [
    path("", include(router.urls)),
]
