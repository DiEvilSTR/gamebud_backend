from django.forms import CharField
from user_profile.models import bio_field_constraints, nickname_field_constraints
from utils.validation.exact_form import ExactForm

nickname_constraints = { 'max_length': nickname_field_constraints['max_length'], 'required': False }
bio_constraints = { 'max_length': bio_field_constraints['max_length'], 'required': False }


class UserSettingsForm(ExactForm):
    nickname = CharField(**nickname_constraints)
    bio = CharField(**bio_constraints)
    