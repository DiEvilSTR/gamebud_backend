from django.db import models


title_field_constraints = {
    'max_length': 42,
}

description_field_constraints = {
    'max_length': 1000,
    'blank': True,
}


class GameGenre(models.Model):
    title = models.CharField(**title_field_constraints)
    description = models.TextField(**description_field_constraints)
    
    def __str__(self):
        return self.title
