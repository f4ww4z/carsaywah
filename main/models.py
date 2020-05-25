from django.db import models


# Create your models here.

class Car(models.Model):
    platNo = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    capacity = models.IntegerField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Booking(models.Model):
    platNo = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
