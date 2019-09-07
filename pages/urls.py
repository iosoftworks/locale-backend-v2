
from django.urls import path

from .views import EmergencyPageView, MapsPageView

urlpatterns = [
    path('emergency/', EmergencyPageView.as_view(), name='emergency'),
    path('maps/', MapsPageView.as_view(), name='maps'),
]
