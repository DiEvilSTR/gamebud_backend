from django.contrib.auth.models import User, auth
from enum import Enum

from utils.http.responses.JSONResponse import JSONResponse

from .forms import UserProfileForm
from .models import UserProfile

class HttpResponseStatus(Enum):
    BAD_REQUEST=400
    NOT_FOUND=404

class HttpRequestErrorCode(Enum):
    USER_EXISTS=1
    ENTITY_CREATION_ERROR=2
    VALIDATION_ERROR=3


def private_user_profile(request):
    user = request.user
    user_profile = UserProfile.objects.values('nickname', 'bio', 'created_at').get(user=user.id)

    return JSONResponse(user_profile)


def signup(request):
    username = request.POST['username']
    nickname = request.POST['nickname']
    password = request.POST['password']
    
    # TODO: Add form validation
    # TODO: Add POST method validation

    if User.objects.filter(username=username).exists():
        data = {
            'error': 'Username is already taken',
            'error_code': HttpRequestErrorCode.USER_EXISTS.value,
        }

        return JSONResponse(data, status=HttpResponseStatus.BAD_REQUEST.value)
    
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

        data = {
            'error': 'User creation error',
            'error_code': HttpRequestErrorCode.ENTITY_CREATION_ERROR.value,
        }

        return JSONResponse(data, status=HttpResponseStatus.BAD_REQUEST.value)

    data = { 'profile': user_profile }

    return JSONResponse(data)


def settings(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user.id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        
        if not form.is_valid():
            data = {
                'error': 'Validation error',
                'error_code': HttpRequestErrorCode.VALIDATION_ERROR.value,
            }

            return JSONResponse(data, status=HttpResponseStatus.BAD_REQUEST.value)
        
        nickname = request.POST.get('nickname', user_profile.nickname)
        bio = request.POST.get('bio', user_profile.bio)
        
        user_profile.nickname = nickname
        user_profile.bio = bio

        user_profile.save()
    
    key_list = ['nickname', 'bio', 'created_at']
    data = { key: user_profile.__dict__[key] for key in key_list }

    return JSONResponse(data)
