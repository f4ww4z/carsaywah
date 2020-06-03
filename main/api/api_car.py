from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Car
from main.permissions import IsOwnerOrReadOnly
from main.serializers import car_serializer


class CarCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = car_serializer.CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
def car_provider_list(request):
    cars_of_current_user = Car.objects.filter(owner=request.user)
    serializer = car_serializer.CarSerializer(cars_of_current_user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_car(request, brand: str):
    searched_cars = Car.objects.exclude(owner=request.user)
    if brand is None or len(brand.strip()) == 0:
        serializer = car_serializer.CarSerializer(searched_cars, many=True)
        return Response(serializer.data)

    searched_cars = searched_cars.filter(brand__icontains=brand)
    serializer = car_serializer.CarSerializer(searched_cars, many=True)
    return Response(serializer.data)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Car.objects.all()
    serializer_class = car_serializer.CarSerializer
