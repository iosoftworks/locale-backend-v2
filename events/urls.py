from django.urls import path

from .views import EventListView, EventDetailView

urlpatterns = [
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('', EventListView.as_view(), name='home'),
]