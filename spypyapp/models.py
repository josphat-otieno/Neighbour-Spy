from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbor(models.Model):
    name =models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    occupants_count = models.IntegerField(default=1)

    def __str__(self):
        return self.name

