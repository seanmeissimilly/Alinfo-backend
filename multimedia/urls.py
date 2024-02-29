from django.urls import path
from multimedia import views
from django.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"", views.MultimediaView, "multimedia")
router.register(
    r"classification", views.MultimediaclassificationView, "multimediaclassification"
)

urlpatterns = [
    path("", include(router.urls)),
]
