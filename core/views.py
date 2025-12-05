from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Team

class list_teams(ListView):
    model = Team
    template_name = 'core/home.html'
    context_object_name = 'teams'

class detail_team(DetailView):
    model = Team
    template_name = 'core/detail_team.html'
    context_object_name = 'team'
    slug_field = 'pk' \

class add_team(CreateView):
    model = Team
    