from django.db.models import Count

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.decorators.views.view import view
from games.models.game import Game

from .game_list_form import GameListGetForm

default_count = 25

@view(get=GameListGetForm)
def game_list_view(request, data):
    count = data.get('count', default_count)
    game_list = Game.objects.values('id', 'title').annotate(game_genres_count=Count('genre_list'))[:count]
    game_list_data = list(game_list)
    
    return JSONResponse(game_list_data)