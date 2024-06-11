from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from competitions.models import AgeCategory, Competition, Season
from clubs.models import Team


class Venue(models.Model):
    name = models.CharField(
        max_length=254,
        null=False,
        blank=False
    )

    short_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    street_address = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    city = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    map_url = models.URLField(
        max_length=1024,
        null=False,
        blank=False
    )
    
    last_updated = models.DateTimeField(
        auto_now=timezone.now
    )

    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.short_name
    

class Game(models.Model):
    game_id = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
    )
    
    season = models.ForeignKey(
        Season,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    home_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        related_name="home_team"
    )
    
    away_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        related_name="away_team"
    )
    
    date_time = models.DateTimeField(
        default=timezone.now,
        blank=True
    )
    
    venue = models.ForeignKey(
        Venue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    referee_a = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="referee_a"
    )
    
    referee_b = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    notes = models.TextField(
        max_length=1024,
        blank=True
    )
    
    last_updated = models.DateTimeField(
        auto_now=timezone.now
    )
    
    def __str__(self):
        return f"[{self.game_id}] {self.home_team} - {self.away_team}"
    
    class Meta:
        ordering = ["date_time"]


class GameApplication(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
    )
    
    ref_application = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )