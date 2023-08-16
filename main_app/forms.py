from django.forms import ModelForm
from .models import Comment, Event

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment', 'attending']


