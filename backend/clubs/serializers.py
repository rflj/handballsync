from rest_framework import serializers
from .models import Club, Team
from competitions.serializers import CompetitionSerializer
from competitions.models import Competition


class TeamSerializer(serializers.ModelSerializer):
    competition = serializers.PrimaryKeyRelatedField(queryset=Competition.objects.all())
    competition_details = CompetitionSerializer(source='competition', read_only=True)
    
    class Meta:
        model = Team
        fields = ("id", "club", "name", "deputy", "competition", "competition_details", "last_updated")

class ClubSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, required=False)
    class Meta:
        model = Club
        fields = ("id", "name", "city", "country", "badge_url", "badge", "website_url", "teams")