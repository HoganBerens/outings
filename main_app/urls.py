from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signup/", views.signup, name="signup"),
    path("events/", views.events_index, name="index"),
    path("events/create/", views.EventCreate.as_view(), name="events_create"),
    path('events/<int:event_id>/', views.events_detail, name = 'detail'),
    path('events/<int:event_id>/add_comment/', views.add_comment, name = 'add_comment')
    
]
