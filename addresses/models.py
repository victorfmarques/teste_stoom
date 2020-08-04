import requests
import json

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from teste_stoom.settings import GOOGLE_GEOCODING_API_KEY

class Address(models.Model):
    street_name     = models.CharField(max_length=100, null=False)
    number          = models.IntegerField(null=False)
    complement      = models.CharField(max_length=250, blank=True)
    neighbourhood   = models.CharField(max_length=50, null=False)
    city            = models.CharField(max_length=100, null=False)
    state           = models.CharField(max_length=50, null=False)
    country         = models.CharField(max_length=100, null=False)
    zipcode         = models.IntegerField(null=False)
    latitude        = models.DecimalField(max_digits=15, decimal_places=13, blank=True, null=True)
    longitude       = models.DecimalField(max_digits=15, decimal_places=13, blank=True, null=True)

    def __str__(self):
        return (f'{self.street_name} {self.number}  {self.neighbourhood} {self.city} {self.state} {self.country}')

    class Meta:
        ordering = ('-country', '-state', '-city', '-neighbourhood', '-street_name', '-complement')


@receiver(pre_save, sender=Address)
def google_geocode_lat_and_lng(sender, instance, **kwargs):
    if not (instance.latitude and instance.longitude):
        params = {
            'address' : slugify(instance.__str__()),
            'key' : GOOGLE_GEOCODING_API_KEY
        }
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)
        
        json_response = json.loads(r.text)
            
        try:
            dict_location = json_response['results'][0]['geometry']['location']
            instance.latitude = dict_location['lat']
            instance.longitude= dict_location['lng']
        except IndexError as e:
            return None
            
        
        
        
        
