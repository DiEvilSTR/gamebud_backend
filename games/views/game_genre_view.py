from django.db.models import Count

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.decorators.views.view import view
from games.models.game_genre import GameGenre

from utils.validation.no_data_form import NoDataForm
from utils.http.constants import HttpStatus


@view(get=NoDataForm)
def game_genre_view(request, id):
    try:
        game_genre_data = GameGenre.objects.values('id', 'title', 'description').annotate(games_count=Count('games')).get(id=id)
    except GameGenre.DoesNotExist:
        return JSONResponse(error='', status=HttpStatus.NOT_FOUND)

    return JSONResponse(game_genre_data)
