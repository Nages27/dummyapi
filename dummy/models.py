from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class User(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    completed=models.BooleanField()
    
