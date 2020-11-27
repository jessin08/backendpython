from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User1

class UserViewSet(viewsets.ModelViewSet):
    queryset = User1.objects.all().order_by('name')
    serializer_class = UserSerializer
