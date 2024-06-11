from django.db import models
from django.utils import timezone

class Season(models.Model):
    name = models.CharField(
        max_length=254,
        null=False,
        blank=False,
    )
    
    date_start = models.DateField(
        null=True,
        blank=True
    )
    
    date_end = models.DateField(
        null=True,
        blank=True
    )
    
    is_active = models.BooleanField(
        default=False,
    )
    
    last_updated = models.DateTimeField(
        auto_now=timezone.now
    )
    
    def __str__(self):
        return self.name

class AgeCategory(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    last_updated = models.DateTimeField(
        auto_now=timezone.now
    )
    
    def __str__(self) -> str:
        return self.name
    

class Competition(models.Model):
    name = models.CharField(
        max_length=254,
        null=False,
        blank=False
    )
    
    last_updated = models.DateTimeField(
        auto_now=timezone.now
    )

    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name="season"
    )
    
    age_category = models.ForeignKey(
        AgeCategory,
        on_delete=models.CASCADE,
        related_name="age_category"
    )
    
    def __str__(self):
        return self.name
    


