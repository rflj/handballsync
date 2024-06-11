from django.test import TestCase

from .models import Venue, AgeCategory, Competition, Season, Game
from teams.models import Club, Team


class VenueModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Venue.objects.create(
            name="Hala Legionów Kielce",
            short_name="Hala Legionów",
            city="Kielce",
            map_url="https://goo.gl/maps/dEv4wpmjZYWjoX8CA"
        )

    def test_venue_string_method_returns_name(self):
        """Test Venue name string method"""
        venue = Venue.objects.get(id=1)
        self.assertEqual(str(venue), "Hala Legionów Kielce")

    def test_get_short_name_method_returns_short_name(self):
        venue = Venue.objects.get(id=1)
        self.assertEqual(venue.get_short_name(), "Hala Legionów")

    def test_get_map_url(self):
        venue = Venue.objects.get(id=1)
        self.assertEqual(venue.map_url, "https://goo.gl/maps/dEv4wpmjZYWjoX8CA")
        
class AgeCategoryTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        AgeCategory.objects.create(
            name="Junior"
        )
    
    def test_age_category_string_method_returns_name(self):
        age_cat = AgeCategory.objects.get(id=1)
        self.assertEqual(str(age_cat), "Junior")
        
class CompetitionTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Competition.objects.create(name="EHF Champions League")
    
    
    def test_competiion_string_method_returns_name(self):
        competition = Competition.objects.get(id=1)
        self.assertEqual(str(competition), "EHF Champions League")
        

class SeasonTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Season.objects.create(name="2022/2023", is_active=True)
    
    def test_season_string_method_returns_name(self):
        season = Season.objects.get(id=1)
        self.assertEqual(str(season), "2022/2023")
    
    def test_season_is_active_season(self):
        season = Season.objects.get(id=1)
        self.assertEqual(season.is_active, True)
        

class GameTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.club = Club.objects.create(name="Test Club")
        cls.home_team = Team.objects.create(club=cls.club, name="Home Team")
        cls.away_team = Team.objects.create(club=cls.club, name="Away Team")
        cls.age_category = AgeCategory.objects.create(name="Junior")
        cls.competition = Competition.objects.create(name="Junior league")
        cls.season = Season.objects.create(name="2022/2023")
        cls.venue = Venue.objects.create(name="Camp Nou")
        cls.game = Game.objects.create(
            game_id="M1",
            age_category=cls.age_category,
            competition=cls.competition,
            season=cls.season,
            home_team=cls.home_team,
            away_team=cls.away_team,
            venue=cls.venue
        )
    
    def test_game_string_method_returns_game_name(self):
        self.assertEqual(str(self.game), "[M1] Home Team - Away Team")
    
    def test_game_home_team_returns_team_name(self):
        self.assertEqual(str(self.game.home_team), "Home Team")
        
    def test_game_away_team_returns_team_name(self):
        self.assertEqual(str(self.game.away_team), "Away Team")
    
    def test_game_age_category_returns_age_category_name(self):
        self.assertEqual(str(self.game.age_category), "Junior")
        
    def test_game_competition_returns_competition_name(self):
        self.assertEqual(str(self.game.competition), "Junior league")
    
    def test_game_season_returns_season_name(self):
        self.assertEqual(str(self.game.season), "2022/2023")

    def test_game_veneus_returns_venue_name(self):
        self.assertEqual(str(self.game.venue), "Camp Nou")