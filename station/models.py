from django.db import models
from django.contrib.auth import get_user_model


class Station(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Route(models.Model):
    source = models.ForeignKey(
        to=Station, on_delete=models.CASCADE, related_name="routes_source"
    )
    destination = models.ForeignKey(
        to=Station, on_delete=models.CASCADE, related_name="routes_destination"
    )
    distance = models.IntegerField()

    def __str__(self):
        return f"{self.source} to {self.destination}"


class TrainType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Train(models.Model):
    name = models.CharField(max_length=255)
    cargo_num = models.IntegerField()
    places_in_cargo = models.IntegerField()
    train_type = models.ForeignKey(
        to=TrainType, on_delete=models.CASCADE, related_name="trains"
    )

    def __str__(self):
        return self.name


class Crew(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Journey(models.Model):
    crews = models.ManyToManyField(to=Crew, related_name="journeys")
    route = models.ForeignKey(
        to=Route, on_delete=models.CASCADE, related_name="journeys"
    )
    train = models.ForeignKey(
        to=Train, on_delete=models.CASCADE, related_name="journeys"
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.route} by {self.train}"

    class Meta:
        ordering = ["-departure_time"]


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, related_name="orders"
    )

    def __str__(self):
        return f"N.{self.id}"

    class Meta:
        ordering = ["-created_at"]


class Ticket(models.Model):
    cargo = models.IntegerField()
    seat = models.IntegerField()
    journey = models.ForeignKey(
        to=Journey, on_delete=models.CASCADE, related_name="tickets"
    )
    order = models.ForeignKey(
        to=Order, on_delete=models.CASCADE, related_name="tickets"
    )

    def __str__(self):
        return f"Seat: {self.seat} to {self.journey}"
