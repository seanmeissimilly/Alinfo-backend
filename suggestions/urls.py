from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from suggestions import views


router = routers.DefaultRouter()
router.register(r"", views.SuggestionView)

urlpatterns = [
    path("", include(router.urls)),
]
