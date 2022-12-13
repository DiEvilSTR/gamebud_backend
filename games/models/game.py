from django.db import models
from .game_genre import GameGenre


title_field_constraints = {
    'max_length': 42,
}

description_field_constraints = {
    'max_length': 1000,
    'blank': True,
}

genre_list_field_constraints = {
    'related_name': 'games',
}


class Game(models.Model):
    title = models.CharField(**title_field_constraints)
    description = models.TextField(**description_field_constraints)
    genre_list = models.ManyToManyField(GameGenre, **genre_list_field_constraints)
    
    def __str__(self):
        return f'{self.title} [{self.genre_list.all()[0]}]'