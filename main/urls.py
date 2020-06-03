from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from main.api import api_user, api_car, api_trip

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
    path('trips/', api_trip.CreateTrip.as_view(), name='booking_create'),
    path('mytrips/', api_trip.trip_list, name='booking_list'),
    path('trips/<int:pk>/', api_trip.TripDetail.as_view(), name='booking_detail'),
    path('trips/<int:trip_id>/disable/', api_trip.disable_trip, name='booking_disable'),
]
