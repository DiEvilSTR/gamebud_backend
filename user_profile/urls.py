from django.urls import path

from .views import get_csrf_token, private_user_profile, signup

private_user_profile_url = 'private_user_profile'
signup_url = 'signup'
csrf_token_url = 'csrf'

urlpatterns = [
    path(private_user_profile_url, private_user_profile, name=private_user_profile_url),
    path(signup_url, signup, name=signup_url),
    path(csrf_token_url, get_csrf_token, name=csrf_token_url),
]