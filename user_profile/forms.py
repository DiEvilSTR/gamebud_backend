from django.forms import CharField, Form
from .models import UserProfile


class UserProfileForm(Form):
    nickname = CharField(**UserProfile.nickname)
    bio = CharField(**UserProfile.bio)