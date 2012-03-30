#coding=utf-8

from django.db import models

class Country(models.Model):
	name = models.CharField(verbose_name='Pays', unique=True, max_length=50)
	
	class Meta:
		verbose_name_plural ='Pays'
		
	def __unicode__(self):
		return self.name
		
class Category(models.Model):
	label = models.CharField(verbose_name='Catégorie', unique=True,  max_length=50)
	
	class Meta:
		verbose_name_plural ='Catégories'
		
	def __unicode__(self):
		return self.label

class SubCategory(models.Model):
	label = models.CharField(verbose_name='Thème', unique=True, max_length=50)
	
	class Meta:
		verbose_name_plural ='Thèmes'
		
	def __unicode__(self):
		return self.label

class Item(models.Model):
	
	country = models.ForeignKey(Country, verbose_name='Pays')
	category = models.ForeignKey(Category, verbose_name='Catégorie')
	subcategory = models.ForeignKey(SubCategory, verbose_name='Thème')
	label = models.CharField(verbose_name='Titre', max_length=50)
	image = models.ImageField(upload_to='pictures')
	with_chip = models.BooleanField(verbose_name='Avec ou sans puce', blank=True)
	units = models.CharField(verbose_name="Nombre d'unités", max_length=50, blank=True)
	emissionDate = models.CharField(verbose_name="Année d'émission", max_length=10, blank=True)
	expirationDate = models.CharField(verbose_name="Année d'expiration", max_length=10, blank=True)
	numberOfCopies = models.CharField(verbose_name='Tirage', max_length=50, blank=True)
	
	
	class Meta:
		verbose_name_plural ='Items'
	
	def __unicode__(self):
		return '%s %s %s %s' % (self.country.name, self.category.label, self.subcategory.label, self.label)