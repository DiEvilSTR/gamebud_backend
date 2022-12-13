from django.forms import IntegerField
from utils.validation.exact_form import ExactForm

count_constraints = { 'max_value': 100, 'min_value': 1, 'required': False }


class GameListGetForm(ExactForm):
    count = IntegerField(**count_constraints)