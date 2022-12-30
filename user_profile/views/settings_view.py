from django.db.models import Model, QuerySet
from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod
from utils.http.decorators.views.view import view
from utils.validation.no_data_form import NoDataForm
from games.models.game import Game
from user_profile.models import UserProfile

from .settings_form import UserSettingsForm

from django.db.models import Subquery, Value
from django.db import connection

class DataExtractor:
    model: Model = None

    field_list: list[str] = []

    def extract(self, **kwargs):
        model_instance = self.model.objects.get(**kwargs)

        result = {}

        for field in self.field_list:
            # TODO: Add related field handling (one-2-many, many-2-many)

            field_value = model_instance.__dict__[field]

            result[field] = field_value 

        return result
    

class UserProfileDataExtractor(DataExtractor):
    model = UserProfile

    field_list = ['nickname', 'bio']

@view(get=NoDataForm, patch=UserSettingsForm)
def settings_view(request, data=None):
    user_id = request.user.id
    user_profile = UserProfile.objects.get(user=user_id)

    qwe = UserProfileDataExtractor().extract(user=user_id)

    if request.method == HttpMethod.PATCH:
        nickname = data.get('nickname', user_profile.nickname)
        bio = data.get('bio', user_profile.bio)
        
        user_profile.nickname = nickname
        user_profile.bio = bio

        user_profile.save()

    # qwe = {
    #     'nickname': user_profile.nickname,
    #     'bio': user_profile.bio,
    #     'favorite_game_list': list(user_profile.favorite_game_list.values('id', 'title').all()),
    # }

    # user_profile_data = UserProfile.objects.values('bio').annotate(favorite_game_list=Value('favorite_game_list__title')).get(user=user.id)
    
    # favorite_game_list = user_profile.favorite_game_list.values('id', 'title').all()
    # user_profile_data = user_profile.objects.values('nickname', 'bio', 'created_at')
    # user_data = {key: user_profile.__dict__[key] for key in ['nickname', 'bio', 'created_at']}
    # qwe = {**user_data,'favorite_game_list': list(favorite_game_list)}

    return JSONResponse(qwe)
    # return JSONResponse(connection.queries)
    # return JSONResponse(favorite_game_list)
    # return JSONResponse(user_data)
