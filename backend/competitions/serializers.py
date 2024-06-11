from rest_framework import serializers
from .models import AgeCategory, Competition, Season

class AgeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeCategory
        fields = ("__all__")

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ("__all__")

class CompetitionSerializer(serializers.ModelSerializer):
    season = SeasonSerializer(read_only=True)
    age_category = AgeCategorySerializer(read_only=True)
    class Meta:
        model = Competition
        fields = ("__all__")