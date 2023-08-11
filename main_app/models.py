from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SPORTS = (("F", "Football"), ("B", "Basketball"), ("B", "Baseball"))


class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sport = models.CharField(max_length=1, choices=SPORTS, default=SPORTS[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
