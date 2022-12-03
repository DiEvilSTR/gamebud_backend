from django.forms import CharField, Form
from .models import bio_field_constraints, nickname_field_constraints

def convert_constraints(constraints: object) -> object:
    form_constraints = {}
    
    for key in constraints.keys():
        value = constraints[key]
        
        if key == 'blank':
            continue
        else:
            form_constraints[key] = value

    return form_constraints

nickname_constraints = convert_constraints({ **nickname_field_constraints, 'required': False })
bio_constraints = convert_constraints({ **bio_field_constraints, 'required': False })

class UserProfileForm(Form):
    nickname = CharField(**nickname_constraints)
    bio = CharField(**bio_constraints)
