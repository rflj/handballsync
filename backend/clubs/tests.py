from django.test import TestCase
from .models import Club, Team


class ClubModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up -non-modified objects used by all test methods
        Club.objects.create(name="Vive Kielce", city="Kielce")

    def test_club_string_method_returns_name(self):
        """Test club name string method"""
        club = Club.objects.get(id=1)
        self.assertEqual(str(club), "Vive Kielce")


class TeamModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up -non-modified objects used by all test methods
        club = Club.objects.create(name="Vive Kielce", city="Kielce")
        Team.objects.create(name="Vive II Kielce")

    def test_club_string_method_return_name(self):
        team = Team.objects.get(id=1)
        self.assertEqual(str(team), "Vive II Kielce")