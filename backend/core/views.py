from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date
from matches.models import Game
from competitions.models import Season

class IndexView(generic.TemplateView):
    """View class for home page"""
    template_name = "core/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["game_list"] = Game.objects.filter(season__is_active=True)
        context["season"] = Season.objects.get(is_active=True)
        return context