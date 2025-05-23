from django.contrib.auth.models import User
from django.db import models

class Pilot(models.Model):
    RANK_CHOICES = [
        ("J", "Junior"),
        ("I", "Intermediate"),
        ("S", "Senior")
    ]

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_year = models.IntegerField()
    flight_hours = models.FloatField()
    rank = models.CharField(max_length=1, choices=RANK_CHOICES)

    def __str__(self):
        return self.name

class Balloon(models.Model):
    TYPE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large")
    ]

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    manufacturer = models.CharField(max_length=50)
    max_passengers = models.IntegerField()

    def __str__(self):
        return self.name

class Airline(models.Model):
    name = models.CharField(max_length=50)
    founding_year = models.IntegerField()
    flies_outside_europe = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=50, unique=True)
    take_off_airport = models.CharField(max_length=50)
    landing_airport = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flights/')
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight_number} - {self.take_off_airport} - {self.landing_airport}'

class AirlinePilot(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pilot} - {self.airline}'
