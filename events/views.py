from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Event

# Create your views here.

class EventListView(ListView):
    model = Event
    template_name = 'home.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'

class EventCreateView(CreateView):
    model = Event
    template_name = 'event_new.html'
    fields = ['day', 'title', 'description', 'start_time', 'end_time', 'location', 'price']

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'event_edit.html'
    fields = ['day', 'title', 'description', 'start_time', 'end_time', 'location', 'price']

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('home')