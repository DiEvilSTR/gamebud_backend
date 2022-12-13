from django.db.models import Count

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.decorators.views.view import view
from games.models.game import Game

from utils.validation.no_data_form import NoDataForm
from utils.http.constants import HttpStatus


@view(get=NoDataForm)
def game_view(request, id):
    try:
        game_data = Game.objects.values('id', 'title', 'description').get(id=id)
    except Game.DoesNotExist:
        return JSONResponse(error='', status=HttpStatus.NOT_FOUND)

    return JSONResponse(game_data)