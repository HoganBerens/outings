from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signup/", views.signup, name="signup"),
    path("events/", views.events_index, name="index"),
    path("events/create/", views.EventCreate.as_view(), name="events_create"),
    path("events/<int:pk>/update/", views.EventUpdate.as_view(), name="events_update"),
    path("events/<int:pk>/delete/", views.EventDelete.as_view(), name="events_delete"),
    path("events/<int:event_id>/", views.events_detail, name="detail"),
    path("events/<int:event_id>/add_comment/", views.add_comment, name="add_comment"),
    path("events/myevents/", views.my_events, name="my_events"),
    path('events/<int:event_id>/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('events/<int:event_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
