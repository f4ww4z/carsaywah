from django.contrib.auth.models import User
from rest_framework import generics, permissions

from main.serializers import user_serializer


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer.UserViewSerializer


class UserCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = user_serializer.UserCreateSerializer
