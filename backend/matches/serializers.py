from rest_framework import serializers
from .models import Game

class GameListSerializer(serializers.ModelSerializer):
    home_team_name = serializers.CharField(source="home_team.name")
    away_team_name = serializers.CharField(source="away_team.name")
    competition_name = serializers.CharField(source="competition.name")
    ref_a_last_name = serializers.CharField(source="referee_a.last_name")
    ref_b_last_name = serializers.CharField(source="referee_b.last_name")


    class Meta:
        model = Game
        fields = ("game_id", "competition_name", "home_team_name", "away_team_name", "date_time", "ref_a_last_name", "ref_b_last_name")