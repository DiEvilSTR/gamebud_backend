from django.contrib.auth.models import User, auth
from django.middleware.csrf import get_token
from enum import Enum

from utils.http.decorators.json_api import json_api
from utils.http.formatters.to_json_response import to_json_response

from .models import UserProfile

class HttpResponseStatus(Enum):
    BAD_REQUEST=400
    NOT_FOUND=404

class HttpRequestErrorCode(Enum):
    USER_EXISTS=1


@json_api
def private_user_profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user.id)

    return user_profile


@json_api
def signup(request):
    username = request.POST['username']
    nickname = request.POST['nickname']
    password = request.POST['password']
    
    # TODO: Add form validation
    # TODO: Add POST method validation

    if User.objects.filter(username=username).exists():
        data = {
            'error': 'Username is already taken',
            'error_code': HttpRequestErrorCode.USER_EXISTS,
        }

        return to_json_response(data, status=HttpResponseStatus.BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password)
    user.save()

    #log user in and redirect to settings page
    user_login = auth.authenticate(username=username, password=password)
    auth.login(request, user_login)

    #create a UserProfile object for the new user
    user_profile = UserProfile.objects.create(nickname=nickname, user=user.id)
    user_profile.save()
    
    return { 'profile': user_profile }

@json_api
def get_csrf_token(request):
    return { 'token': get_token(request) }