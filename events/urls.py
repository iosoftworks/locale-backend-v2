from django.urls import path

from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView

urlpatterns = [
    
    path('event/new/', EventCreateView.as_view(), name='event_new'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('', EventListView.as_view(), name='home'),
]