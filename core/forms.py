from django.forms import ModelForm
from django import forms
from .models import Team, Pokemon

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description']

class PokemonForm(ModelForm):

    class Meta:
        model = Pokemon
        fields = ['nickname', 'level', 'pokedex_number','image_url','attack','defense','type']