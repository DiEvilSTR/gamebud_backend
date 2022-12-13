from django.contrib import admin

from .models.game import Game
from .models.game_genre import GameGenre


admin.site.register(Game)
admin.site.register(GameGenre)