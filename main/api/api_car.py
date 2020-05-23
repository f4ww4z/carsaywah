from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.permissions import IsOwnerOrReadOnly

from main.serializers import car_serializer
from main.models import Car


class CarCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = car_serializer.CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
def car_list(request):
    cars_of_current_user = Car.objects.all().filter(owner=request.user)
    serializer = car_serializer.CarSerializer(cars_of_current_user, many=True)
    return Response(serializer.data)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Car.objects.all()
    serializer_class = car_serializer.CarSerializer
