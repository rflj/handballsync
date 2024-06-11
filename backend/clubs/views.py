from rest_framework import viewsets
from .serializers import ClubSerializer, TeamSerializer

from django.shortcuts import render
from django.views import generic

from .models import Club, Team


class ClubListView(generic.ListView):
    """View for club list page"""
    model = Club
    context_object_name = 'club_list'
    queryset = Club.objects.all()

class ClubDetailView(generic.DetailView):
    """View for club details page"""
    model = Club

class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()