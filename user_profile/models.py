from django.db import models
from django.contrib.auth.models import User

user_field_constraints = {
    'on_delete': models.CASCADE,
    'primary_key': True,
}

nickname_field_constraints = {
    'max_length': 42,
}

bio_field_constraints = {
    'max_length': 500,
    'blank': True,
}

class UserProfile(models.Model):
    user = models.OneToOneField(User, **user_field_constraints)
    nickname = models.CharField(**nickname_field_constraints)
    bio = models.TextField(**bio_field_constraints)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return self.nickname