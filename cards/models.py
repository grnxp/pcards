#coding=utf-8

from django.db import models

class Country(models.Model):
	name = models.CharField(verbose_name='Pays', max_length=50)
	
	class Meta:
		verbose_name_plural ='Pays'
		
class Category(models.Model):
	label = models.CharField(verbose_name='Catégorie', max_length=50)
	
	class Meta:
		verbose_name_plural ='Catégories'

class SubCategory(models.Model):
	label = models.CharField(verbose_name='Thème', max_length=50)
	
	class Meta:
		verbose_name_plural ='Thèmes'

class Item(models.Model):
	
	country = models.ForeignKey(Country, verbose_name='Pays')
	category = models.ForeignKey(Category, verbose_name='Catégorie')
	subcategory = models.ForeignKey(SubCategory, verbose_name='Thème')
	label = models.CharField(verbose_name='Titre', max_length=50)
	image = models.ImageField(upload_to='pictures')
	with_chip = models.BooleanField(verbose_name='Avec ou sans puce')
	units = models.IntegerField(verbose_name="Nombre d'unités")
	emissionDate = models.DateTimeField(verbose_name="Année d'émission")
	expirationDate = models.DateTimeField(verbose_name="Année d'expiration")
	numberOfCopies = models.IntegerField(verbose_name='Tirage')
	
	
	class Meta:
		verbose_name_plural ='Items'