from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.permissions import IsOwnerOrReadOnly

from main.serializers import booking_serializer
from main.models import Booking


class CreateBooking(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = booking_serializer.BookingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
def booking_list(request):
    bookings_of_current_user = Booking.objects.all().filter(owner=request.user)
    serializer = booking_serializer.BookingSerializer(bookings_of_current_user, many=True)
    return Response(serializer.data)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Booking.objects.all()
    serializer_class = booking_serializer.BookingSerializer
