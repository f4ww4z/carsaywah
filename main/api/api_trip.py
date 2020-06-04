from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Trip
from main.permissions import IsRenterOrReadOnly
from main.serializers import trip_serializer


class CreateTrip(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = trip_serializer.TripSerializer

    def perform_create(self, serializer):
        serializer.save(renter=self.request.user, status='Active')


@api_view(['GET'])
def trip_list(request):
    trip_of_current_user = Trip.objects.filter(renter=request.user)
    serializer = trip_serializer.TripViewSerializer(trip_of_current_user, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def disable_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip.status = 'Finished'
    trip.save()
    serializer = trip_serializer.TripSerializer(trip)
    return Response(serializer.data)


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRenterOrReadOnly]
    queryset = Trip.objects.all()
    serializer_class = trip_serializer.TripSerializer
