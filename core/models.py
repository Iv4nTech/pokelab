from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50)
    colour_hex = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"
    
class Pokemon(models.Model):
    nickname = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    pokedex_number = models.IntegerField()
    image_url = models.URLField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    type = models.ManyToManyField(Type)

    def __str__(self) -> str:
        return f"{self.nickname}"
