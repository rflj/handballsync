from rest_framework import viewsets

from django.shortcuts import render

from .serializers import UserProfileSerializer
from .models import UserProfile

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()