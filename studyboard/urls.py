"""URL patterns for the Study Resources Board project."""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("resources.urls")),
]
