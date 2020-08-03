from django.db import models


class Address(models.Model):
    street_name     = models.CharField(max_length=100, null=False, blank=False)
    number          = models.IntegerField(null=False, blank=False)
    complement      = models.CharField(max_length=250)
    neighbourhood   = models.CharField(max_length=50, null=False, blank=False) 
    city            = models.CharField(max_length=100, null=False, blank=False)
    state           = models.CharField(max_length=50, null=False, blank=False)
    country         = models.CharField(max_length=100, null=False, blank=False)
    zipcode         = models.IntegerField(max_length=8, null=False, blank=False)
    latitude        = models.DecimalField(max_length=15, decimal_places=13)
    longitude       = models.DecimalField(max_length=15, decimal_places=13)

    def __str__(self):
        return (f'{self.country} - {self.state} - {self.city} - {self.neighbourhood} - {self.street_name} - {self.number}')

    class Meta:
        ordering = ('-country', '-state', '-city', '-neighbourhood', '-street_name', '-complement')

    