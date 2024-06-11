from django.contrib import admin
from .models import Venue, AgeCategory, Competition, Season, Game


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_name",
        "city"
    )

@admin.register(AgeCategory)
class AgeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    
@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_start",
        "date_end",
        "is_active",
    )
    
    list_filter = (
        "is_active",
    )
    
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "game_id",
        "date_time",
        "home_team",
        "away_team",
        "competition",
        "season",
        "venue",
        "referee_a",
        "referee_b",
    )
    
    list_filter = (
        "home_team",
        "away_team",
        "competition",
        "season",
        "venue"
    )
    
    fields = [
        "season",
        "game_id",
        ("competition"),
        ("home_team", "away_team"),
        "date_time",
        ("referee_a", "referee_b"),
        "venue"
    ]
    
    