from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Team, Pokemon
from .forms import TeamForm, PokemonForm
from django.db.models import Count
from django.urls import reverse_lazy

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
    success_url = reverse_lazy('home')
    template_name = 'core/add_team.html'

class delete_pokemon(DeleteView):
    model = Pokemon
    template_name = 'core/delete_pokemon.html'

    def get_success_url(self):
        id_del_equipo = self.kwargs['team_id']
        return reverse_lazy('detail_team', kwargs={'pk': id_del_equipo})


class add_pokemon(CreateView):
    model = Pokemon
    form_class = PokemonForm
    success_url = reverse_lazy('home')
    template_name = 'core/add_pokemon.html'

class update_team(UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('home')
    template_name = 'core/update_team.html'