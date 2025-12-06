from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', list_teams.as_view(), name='home'),
    path('detail_team/<int:pk>', detail_team.as_view(), name='detail_team'),
    path('add_team/', add_team.as_view(), name='add_team'),
    path('add_pokemon/', add_pokemon.as_view(), name='add_pokemon'),
    path('update_team/<int:pk>/', update_team.as_view(), name='update_team')
]
