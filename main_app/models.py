from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
SPORTS = (
    ("Football", "Football"),
    ("Basketball", "Basketball"),
    ("Baseball", "Baseball"),
)
ATTENDING = (("Y", "Yes"), ("N", "No"))


class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField("Party Date", default="2023-08-28")
    sport = models.CharField(max_length=20, choices=SPORTS, default=SPORTS[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    map_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"event_id": self.id})


class Comment(models.Model):
    comment = models.TextField(max_length=200)
    attending = models.CharField(
        max_length=1, choices=ATTENDING, default=ATTENDING[0][0]
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
