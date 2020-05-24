from django.contrib.auth.models import User
from rest_framework import serializers as ser
from main.models import Car


class CarSerializer(ser.HyperlinkedModelSerializer):
    owner = ser.ReadOnlyField(source='owner.username')
    class Meta:
        model = Car
        fields = ['id','platNo', 'brand', 'capacity', 'owner']
