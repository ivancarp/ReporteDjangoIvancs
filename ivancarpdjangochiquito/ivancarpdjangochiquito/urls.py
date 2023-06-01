from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("djangochiquito/", include("djangochiquito.urls")),
    path("admin/", admin.site.urls),
]
