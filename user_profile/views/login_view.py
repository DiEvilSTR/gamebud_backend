from django.contrib.auth import authenticate, login

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod, HttpStatus
from utils.http.decorators.views.view import view
from utils.constants import SystemErrorCode

from user_profile.models import UserProfile
from .login_form import LoginForm

@view(login_required=False, methods={ HttpMethod.GET: False, HttpMethod.POST: True }, RequestForm=LoginForm)
def login_view(request):
    if request.method == HttpMethod.POST:
        username = request.POST['username']
        password = request.POST['password']

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
