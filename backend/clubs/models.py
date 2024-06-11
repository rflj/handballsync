from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django_countries.fields import CountryField

from competitions.models import Competition


class Club(models.Model):
    """Model representing Club object"""
    name = models.CharField(
        max_length=254,
        help_text="Club name",
        verbose_name="Club name"
    )

    city = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    country = CountryField(default="PL")

    badge_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )

    badge = models.ImageField(
        null=True,
        blank=True
    )

    website_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Team(models.Model):
    """Model representing Team object"""
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name="teams",
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=200,
        help_text="Team name",
        verbose_name="Team name"
    )

    deputy = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE
    )

    last_updated = models.DateTimeField(
        auto_now=timezone.now
    )

    def __str__(self):
        return self.name
