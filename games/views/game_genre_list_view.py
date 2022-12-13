from django.db.models import Count

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.decorators.views.view import view
from games.models.game_genre import GameGenre

from .game_genre_list_form import GameGenreListGetForm

default_count = 25

@view(get=GameGenreListGetForm)
def game_genre_list_view(request, data):
    count = data.get('count', default_count)
    game_genre_list = GameGenre.objects.values('id', 'title').annotate(games_count=Count('games'))[:count]
    game_genre_list_data = list(game_genre_list)
    
    return JSONResponse(game_genre_list_data)