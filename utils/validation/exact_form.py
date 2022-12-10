from django.core.exceptions import ValidationError
from django.forms import Form


class ExactForm(Form):
    def clean(self):
        cd = self.cleaned_data

        allowed_field_list = self.fields
        field_list = dict.keys(self.data)
        
        for field in field_list:
            if field not in allowed_field_list:
                raise ValidationError(f'Unexpected key: {field}')

        return cd