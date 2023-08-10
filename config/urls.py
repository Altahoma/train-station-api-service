from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/station/", include("station.urls", namespace="station")),
    path("__debug__/", include("debug_toolbar.urls")),
]

# todo: add swagger
# todo: pagination
# todo: user and auth
# todo: add JWT
# todo: add tests
# todo: dockerized
