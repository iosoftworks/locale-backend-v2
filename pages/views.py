from django.views.generic import TemplateView

class EmergencyPageView(TemplateView):
    template_name = 'emergency.html'

class MapsPageView(TemplateView):
    template_name = 'maps.html'