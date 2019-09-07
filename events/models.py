from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])
    
    def get_total_price(self):
        return Event.objects.aggregate(Sum('price'))