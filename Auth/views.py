from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CustomUser, Role
from .serializers import UserSerializer, RoleSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
