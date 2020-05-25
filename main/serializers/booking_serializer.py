from django.contrib.auth.models import User
from rest_framework import serializers as ser
from main.models import Booking


class BookingSerializer(ser.HyperlinkedModelSerializer):
    owner = ser.ReadOnlyField(source='owner.username')

    class Meta:
        model = Booking
        fields = ['platNo', 'owner']
