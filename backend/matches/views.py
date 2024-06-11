from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GameListSerializer
from .models import Game

# Create your views here.
class GameListViewSet(viewsets.ModelViewSet):
    serializer_class = GameListSerializer
    queryset = Game.objects.all()