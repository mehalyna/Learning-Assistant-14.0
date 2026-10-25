"""URL patterns for the resources application."""
from django.urls import path

from . import views


urlpatterns = [
    path("", views.resource_list, name="resource_list"),
    path("resources/add/", views.add_resource, name="add_resource"),
    path("resources/<int:pk>/", views.resource_detail, name="resource_detail"),
    path(
        "resources/<int:pk>/delete/",
        views.delete_resource,
        name="delete_resource",
    ),
]
