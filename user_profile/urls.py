from django.urls import path

from .views import private_user_profile, signup, settings

private_user_profile_url = 'private_user_profile'
signup_url = 'signup'
settings_url = 'settings'

urlpatterns = [
    path(private_user_profile_url, private_user_profile, name=private_user_profile_url),
    path(signup_url, signup, name=signup_url),
    path(settings_url, settings, name=settings_url),
]