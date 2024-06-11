from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import AgeCategorySerializer, SeasonSerializer, CompetitionSerializer
from .models import AgeCategory, Season, Competition

class AgeCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    serializer_class = AgeCategorySerializer
    queryset = AgeCategory.objects.all()

class SeasonViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()

class CompetitionsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()