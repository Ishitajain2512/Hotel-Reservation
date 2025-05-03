from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=5, unique=True)
    floor = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.number} (Floor {self.floor})"

class Booking(models.Model):
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    rooms = models.ManyToManyField(Room)
    total_travel_time = models.IntegerField(default=0)

    def __str__(self):
        return f"Booking by {self.guest_name}"
