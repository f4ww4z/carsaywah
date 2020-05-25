from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from main.api import api_user, api_car, api_booking

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', api_user.UsersList.as_view(), name='users_list'),
    path('users/register/', api_user.UserCreate.as_view(), name='user_create'),
    path('cars/', api_car.CarCreate.as_view(), name='car_create'),
    path('mycars/', api_car.car_provider_list, name='car_list'),
    path('searchcar/<str:brand>/', api_car.search_car, name='search_car_list'),
    path('cars/<int:pk>/', api_car.CarDetail.as_view(), name='car-detail'),
    path('bookings/', api_booking.CreateBooking.as_view(), name='booking_create'),
    path('mybookings/', api_booking.booking_list, name='booking_list'),
    path('bookings/<int:pk>/', api_booking.BookingDetail.as_view(), name='booking_detail'),

]
