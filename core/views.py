from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Team, Pokemon
from .forms import TeamForm, PokemonForm
from django.db.models import Count

class list_teams(ListView):
    model = Team
    template_name = 'core/home.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return Team.objects.annotate(num_pokemon=Count('pokemon'))
        

class detail_team(DetailView):
    model = Team
    template_name = 'core/detail_team.html'
    context_object_name = 'team'
    slug_field = 'pk' 

class add_team(CreateView):
    model = Team
    form_class = TeamForm
    success_url = '/home/'
    template_name = 'core/add_team.html'

class add_pokemon(CreateView):
    model = Pokemon
    form_class = PokemonForm
    success_url = '/home/'
    template_name = 'core/add_pokemon.html'