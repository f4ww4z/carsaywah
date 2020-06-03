from rest_framework import serializers as ser

from main.models import Trip


class TripSerializer(ser.ModelSerializer):
    renter = ser.ReadOnlyField(source='renter.username')
    status = ser.ReadOnlyField()

    class Meta:
        model = Trip
        fields = (
            'id', 'renter', 'car', 'startlocation', 'endlocation', 'duration', 'price', 'status')
