from django.urls import path
from .views import package_list_view

urlpatterns = [
    path("", package_list_view, name="package-list-view"),
]