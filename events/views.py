from django.views.generic import ListView

from .models import Event

# Create your views here.

class EventListView(ListView):
    model = Event
    template_name = 'home.html'