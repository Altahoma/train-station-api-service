from django.db import models
from django.contrib.auth import get_user_model


class Station(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Route(models.Model):
    source = models.ForeignKey(
        to=Station, on_delete=models.CASCADE, realted_name="routes"
    )
    destination = models.ForeignKey(
        to=Station, on_delete=models.CASCADE, realted_name="routes"
    )
    distance = models.IntegerField()


class TrainType(models.Model):
    name = models.CharField(max_length=255)


class Train(models.Model):
    name = models.CharField(max_length=255)
    cargo_num = models.IntegerField()
    places_in_cargo = models.IntegerField()
    train_type = models.ForeignKey(
        to=TrainType, on_delete=models.CASCADE, realted_name="trains"
    )


class Crew(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Journey(models.Model):
    crews = models.ManyToManyField(to=Crew, realted_name="journeys")
    route = models.ForeignKey(
        to=Route, on_delete=models.CASCADE, realted_name="journeys"
    )
    train = models.ForeignKey(
        to=Train, on_delete=models.CASCADE, realted_name="journeys"
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, realted_name="orders"
    )


class Ticket(models.Model):
    cargo = models.IntegerField()
    seat = models.IntegerField()
    journey = models.ForeignKey(
        to=Journey, on_delete=models.CASCADE, realted_name="tickets"
    )
    order = models.ForeignKey(
        to=Order, on_delete=models.CASCADE, realted_name="tickets"
    )
