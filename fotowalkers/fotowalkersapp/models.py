from django.db import models

class Spot(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250, blank=False, default='No Title')
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    image = models.URLField(max_length=500, blank=False)
