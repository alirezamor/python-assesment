from unicodedata import name
from django.db import models


class Listing(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    # def __str__(self) -> str:
    #     return self.name


class Room(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='rooms')
    number = models.PositiveIntegerField()


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(format)
    end_time = models.DateTimeField()

    # def __str__(self) -> str:
    #     return self.name
