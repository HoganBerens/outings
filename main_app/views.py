from django.shortcuts import render, redirect
from django import forms
from .models import Event, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
import googlemaps
from googlemaps import Client as GoogleMapsClient
import os

api_key = os.environ.get("GOOGLE_API_KEY")
gmaps = googlemaps.Client(key=api_key)


# Create your views here.



def home(request):
    events = Event.objects.all()
    return render(request, "home.html", {"events": events})


@login_required
def events_index(request):
    events = Event.objects.filter(user=request.user)

    return render(request, "events/index.html", {"events": events})


def filter_sport(request):
    filtered_sport = request.POST["sport"]
    events = Event.objects.filter(sport=filtered_sport)
    return render(request, "home.html", {"events": events})


@login_required
def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    comment_form = CommentForm()
    return render(
        request,
        "events/detail.html",
        {
            "event": event,
            "comment_form": comment_form,
        },
    )


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ["name", "location", "date", "sport", "description"]
    success_url = "/events"

    def form_valid(self, form):
        location = form.cleaned_data["location"]

        map_url = ""

        gmaps_client = GoogleMapsClient(api_key)

        geocode_result = gmaps_client.geocode(location)
        if not geocode_result:
            form.add_error(
                "location", "Location not found, please enter a valid adress."
            )
            return self.form_invalid(form)
        if geocode_result:
            latitude = geocode_result[0]["geometry"]["location"]["lat"]
            longitude = geocode_result[0]["geometry"]["location"]["lng"]

            map_params = {
                "center": f"{latitude},{longitude}",
                "zoom": 12,
                "size": "400x400",
                "markers": f"color:blue|label:D|{latitude},{longitude}",
                "key": api_key,
            }

            map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=12&size=400x400&markers=color:blue|label:D|{latitude},{longitude}&key={api_key}"

        form.instance.map_url = map_url
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ["location", "sport", "description"]


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = "/events"

@login_required
def add_comment(request, event_id):
    form = CommentForm(request.POST)
    event = Event.objects.get(id=event_id)
    if form.is_valid():
        new_comment= form.save(commit=False)
        new_comment.event_id = event_id
        new_comment.save()
        attending_choice = request.POST.get('attending', 'N')
        if attending_choice == 'Y':
            if not event.attendees.filter(id=request.user.id).exists():
                event.attendees.add(request.user)
                return redirect('detail', event_id=event_id)




@login_required
def my_events(request):
    attending_events = Event.objects.filter(attendees=request.user)
    context = {
    'attending_events': attending_events
    }
    return render(request, 'events/myevents.html', context)


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)
