from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod
from utils.http.decorators.views.view import view
from utils.validation.no_data_form import NoDataForm
from games.models.game import Game
from user_profile.models import UserProfile

from .settings_form import UserSettingsForm

from django.db.models import Subquery, Value
from django.db import connection



@view(get=NoDataForm, patch=UserSettingsForm)
def settings_view(request, data=None):
    user = request.user
    game_subquery = Game.objects.values('id', 'title')
    user_profile = UserProfile.objects.get(user=user.id)

    if request.method == HttpMethod.PATCH:
        nickname = data.get('nickname', user_profile.nickname)
        bio = data.get('bio', user_profile.bio)
        
        user_profile.nickname = nickname
        user_profile.bio = bio

        user_profile.save()

    qwe = {
        'nickname': user_profile.nickname,
        'bio': user_profile.bio,
        'favorite_game_list': list(user_profile.favorite_game_list.values('id', 'title').all()),
    }

    user_profile_data = UserProfile.objects.values('bio').annotate(favorite_game_list=Value('favorite_game_list__title')).get(user=user.id)
    
    # favorite_game_list = user_profile.favorite_game_list.values('id', 'title').all()
    # user_profile_data = user_profile.objects.values('nickname', 'bio', 'created_at')
    # user_data = {key: user_profile.__dict__[key] for key in ['nickname', 'bio', 'created_at']}
    # qwe = {**user_data,'favorite_game_list': list(favorite_game_list)}

    return JSONResponse(qwe)
    # return JSONResponse(connection.queries)
    # return JSONResponse(favorite_game_list)
    # return JSONResponse(user_data)
