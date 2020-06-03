from django.contrib.auth.models import User
from rest_framework import serializers as ser
from main.models import Trip


class TripSerializer(ser.HyperlinkedModelSerializer):
    owner = ser.ReadOnlyField(source='owner.username')

    class Meta:
        model = Trip
        fields = ['owner', 'car_id', 'startlocation', 'endlocation', 'duration', 'price', 'active']
