from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod
from utils.http.decorators.views.view import view
from user_profile.models import UserProfile

from .settings_form import UserSettingsForm


@view(methods={ HttpMethod.POST: True }, RequestForm=UserSettingsForm)
def settings_view(request):
    user = request.user

    if request.method == HttpMethod.POST:
        user_profile = UserProfile.objects.get(user=user.id)

        nickname = request.POST.get('nickname', user_profile.nickname)
        bio = request.POST.get('bio', user_profile.bio)
        
        user_profile.nickname = nickname
        user_profile.bio = bio

        user_profile.save()

    user_data = UserProfile.objects.values('nickname', 'bio', 'created_at').get(user=user.id)

    return JSONResponse(user_data)
