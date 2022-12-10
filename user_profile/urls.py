from django.urls import path

from .views.login_view import login_view
from .views.logout_view import logout_view
from .views.settings_view import settings_view
from .views.signup_view import signup_view

login_url = 'login'
logout_url = 'logout'
signup_url = 'signup'
settings_url = 'settings'

urlpatterns = [
    path(login_url, login_view, name=login_url),
    path(logout_url, logout_view, name=logout_url),
    path(signup_url, signup_view, name=signup_url),
    path(settings_url, settings_view, name=settings_url),
]