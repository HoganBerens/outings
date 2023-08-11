from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signup/", views.signup, name="signup"),
    path("events/", views.events_index, name="index"),
    path("events/create/", views.EventCreate.as_view(), name="events_create"),
]
