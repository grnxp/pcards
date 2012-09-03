#coding=utf-8

from django.db import models
from xcards.cards.models import Country

# Create your models here.
class Coordinates(models.Model):
	"""
		Représentation des coordonnées pour un pays au format DD (Degré Décimal) eg. (49.5000 - 123.5000)
	"""
	latitude = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='Latitude')
	longitude = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Longitude')
	country = models.OneToOneField(Country, verbose_name='Pays')
	
	def __unicode__(self):
		return '%s - Lat: %s Long: %s )' % (self.country, str(self.latitude), str(self.longitude))
		
	class Meta:
		verbose_name_plural = 'Coordonnées'
		verbose_name = 'Coordonnées'
