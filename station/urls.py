from django.urls import path, include
from rest_framework import routers

from station.views import (
    StationViewSet,
    RouteViewSet,
    TrainTypeViewSet,
    TrainViewSet,
    CrewViewSet,
    JourneyViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("stations", StationViewSet)
router.register("train-types", TrainTypeViewSet)
router.register("crews", CrewViewSet)
router.register("trains", TrainViewSet)
router.register("orders", OrderViewSet)
router.register("routes", RouteViewSet)
router.register("journeys", JourneyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "station"
