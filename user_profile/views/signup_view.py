from django.contrib.auth.models import User, auth

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod, HttpStatus
from utils.http.decorators.views.view import view
from utils.constants import SystemErrorCode

from user_profile.models import UserProfile
from .signup_form import SignupForm


@view(login_required=False, methods={ HttpMethod.POST: True }, RequestForm=SignupForm)
def signup_view(request):
    username = request.POST['username']
    nickname = request.POST['nickname']
    password = request.POST['password']

    if User.objects.filter(username=username).exists():
        error = {
            'error': 'Username is already taken',
            'error_code': SystemErrorCode.USER_EXISTS,
        }

        return JSONResponse(error=error, status=HttpStatus.BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password)
    user.save()

    # Log user in
    user_login = auth.authenticate(username=username, password=password)
    auth.login(request, user_login)

    try:
        # Create a UserProfile object for the new user
        user_profile = UserProfile.objects.create(nickname=nickname, user=user)
        user_profile.save()
    except:
        user.delete()

        error = {
            'error': 'User creation error',
            'error_code': SystemErrorCode.ENTITY_CREATION_ERROR,
        }

        return JSONResponse(error=error, status=HttpStatus.BAD_REQUEST)

    user_data = UserProfile.objects.values('nickname', 'bio', 'created_at').get(user=user.id)

    return JSONResponse(user_data)
