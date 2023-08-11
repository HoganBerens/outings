from django.shortcuts import render, redirect
from .models import Event, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm


# Create your views here.
def home(request):
    return render(request, "home.html")


@login_required
def events_index(request):
    events = Event.objects.filter(user=request.user)
   
    return render(request, "events/index.html", {"events": events})

@login_required
def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    comment_form = CommentForm()
    return render(request, 'events/detail.html', {
        'event' : event,
        'comment_form': comment_form,
    })


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ["name", "location", "sport", "description"]
    success_url = "/events"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def add_comment(request, event_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment= form.save(commit=False)
    new_comment.event_id = event_id
    new_comment.save()
  return redirect('detail', event_id=event_id)


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
            return redirect("/")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)
