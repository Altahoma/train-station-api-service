from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/station/", include("station.urls", namespace="station")),
    path("__debug__/", include("debug_toolbar.urls")),
]

# todo: add swagger
# todo: add JWT
# todo: add static?
