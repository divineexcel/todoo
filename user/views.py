from django.shortcuts import render

# Create your views here.
from .serializer import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework import TokenObtainPairView
from django.contrib.auth.models import User
from .serializer import RegisterSerializer
from rest_framework import generics



# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer