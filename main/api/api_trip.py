from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.permissions import IsOwnerOrReadOnly

from main.serializers import trip_serializer
from main.models import Trip


class CreateTrip(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = trip_serializer.TripSerializer

    def perform_create(self, serializer):
        serializer.save(renter=self.request.user)


@api_view(['GET'])
def trip_list(request):
    trip_of_current_user = Trip.objects.filter(renter=request.user)
    serializer = trip_serializer.TripSerializer(trip_of_current_user, many=True)
    return Response(serializer.data)


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Trip.objects.all()
    serializer_class = trip_serializer.TripSerializer

