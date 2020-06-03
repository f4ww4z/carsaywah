from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Car(models.Model):
    platNo = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    capacity = models.IntegerField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True)
    bookedBy = models.ForeignKey(User, related_name='%(class)s_bookedBy', on_delete=models.CASCADE, null=True)


class Trip(models.Model):
    car = models.ForeignKey(Car, default=None, on_delete=models.CASCADE)
    startlocation = models.TextField(max_length=255)
    endlocation = models.TextField(max_length=255)
    duration = models.TimeField
    price = models.DecimalField
    active = models.CharField(max_length=20)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
