from django.views.generic import ListView, DetailView

from .models import Event

# Create your views here.

class EventListView(ListView):
    model = Event
    template_name = 'home.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'