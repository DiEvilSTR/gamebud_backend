from django.contrib.auth import authenticate, login

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod, HttpStatus
from utils.http.decorators.views.view import view
from utils.constants import SystemErrorCode

from user_profile.models import UserProfile
from .login_form import LoginForm

@view(login_required=False, post=LoginForm)
def login_view(request, data):
    if request.method == HttpMethod.POST:
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            error = {
                'error': 'Invalid username or password',
                'error_code': SystemErrorCode.INVALID_CREDENTIALS,
            }

            return JSONResponse(error=error, status=HttpStatus.BAD_REQUEST)
        
        login(request, user)

    user_data = UserProfile.objects.values('nickname', 'bio', 'created_at').get(user=user.id)

    return JSONResponse(user_data)
