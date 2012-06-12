#coding=utf-8

from django.db import models

class Country(models.Model):
	label = models.CharField(verbose_name='Pays', unique=True, max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural ='Pays'
		
	def __unicode__(self):
		return self.label
		
class Category(models.Model):
	label = models.CharField(verbose_name='Catégorie', unique=True,  max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural ='Catégories'
		
	def __unicode__(self):
		return self.label

class SubCategory(models.Model):
	label = models.CharField(verbose_name='Thème', unique=True, max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	#category = models.ForeignKey(Category, verbose_name='Catégorie')
	
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
	emissionDate = models.CharField(verbose_name="Année ou date d'émission", max_length=10, blank=True)
	expirationDate = models.CharField(verbose_name="Année ou date d'expiration", max_length=10, blank=True)
	numberOfCopies = models.CharField(verbose_name='Tirage', max_length=50, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)	
	
	class Meta:
		verbose_name_plural ='Cartes de téléphone'
	
	def __unicode__(self):
		return '%s %s %s %s' % (self.country.label, self.category.label, self.subcategory.label, self.label)