#coding=utf-8

from lxml import etree
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#import cards

# HACK: Django doesn’t directly support the use of the ORM outside of
# a Django project. If this module is imported outside of a project
# some environment needs to be set up. See
# http://jystewart.net/process/2008/02/using-the-django-orm-as-a-standalone-component/.
# if 'DJANGO_SETTINGS_MODULE' not in os.environ:
	# sys.path.insert(0, (os.path.dirname(__file__) or '.') + '/../..') # put settings.py on path
	# os.environ['DJANGO_SETTINGS_MODULE'] = 'db.settings'

# from django.db import models

os.environ['DJANGO_SETTINGS_MODULE']='settings'

from django.conf import settings

from django.db import models
from cards.models import *


class GCItem():
	"""
		i.country = attrs.get('gcsfield1')
		i.with_chip = attrs.get('gcsfield2')
		i.image_path = attrs.get('gcsfield3')
		i.subcategory = attrs.get('gcsfield4')
		i.units  = attrs.get('gcsfield5')
		i.label = attrs.get('gcsfield6')
		i.emissionDate = attrs.get('gcsfield7')
		i.expirationDate = attrs.get('gcsfield8')
		i.numberOfCopies = attrs.get('gcsfield10')
		i.category = attrs.get('gcsfield11')
	"""
	country = None
	with_chip = False
	image_path = None
	subcategory = None
	units = None
	label = None
	emissionDate = None
	expirationDate = None
	numberOfCopies = None
	category = None
	gcsid = None
	
	def __str__(self):
		return u'%s / %s / %s / %s' % (self.country, self.category, self.subcategory, self.image_path)
	
	def __unicode__(self):
		return u'%s / %s / %s / %s' % (self.country, self.category, self.subcategory, self.image_path)

def process():
	"""
	Ouvre un fichier GCStar structuré de la manière suivante:
	
		<collection...>
			 <item
			  gcsfield1="France" => pays
			  gcsfield2="1" => avec ou sans puce
			  gcsfield3="france/Alimentation/Gourmandises/milka 50.jpg" => image
			  gcsfield4="Gourmandises" => souscatégorie
			  gcsfield5="50" => unités
			  gcsfield6="Milka Lila Pause" => label
			  gcsfield7="02/1996" => année d'émission
			  gcsfield8="" => date d'expiration
			  gcsfield9="B61013013" => pas utile
			  gcsfield10="1000000" => tirage
			  gcsfield11="Alimentation " => catégorie
			  gcsautoid="19" => nafout
			 >
		</collection>
	"""
	element = etree.parse(r'C:\Dev\xcards\data\collection.gcs')
	items = element.xpath('//collection/item')
	
	my_list = list()
	
	for item in items:
		attrs = item.attrib
	
		i = GCItem()
		i.country = attrs.get('gcsfield1')
		i.with_chip = attrs.get('gcsfield2')
		i.image_path = attrs.get('gcsfield3')
		i.subcategory = attrs.get('gcsfield4')
		i.units  = attrs.get('gcsfield5')
		i.label = attrs.get('gcsfield6')
		i.emissionDate = attrs.get('gcsfield7')
		i.expirationDate = attrs.get('gcsfield8')
		i.numberOfCopies = attrs.get('gcsfield10')
		i.category = attrs.get('gcsfield11')
		i.gcsid = attrs.get('gcsautoid')


		my_list.append(i)
	
	return my_list
	
def insert(aList):
	for item in aList:
		
		print item.gcsid + ' ' + item.country

		# i = Item.objects.get(label=item.label)

		# if i is not None:
		# 	continue

		i = Item() #Item.objects.get_or_create(label=item.label)

		country, created = Country.objects.get_or_create(name=item.country)
		i.country = country

		category, created = Category.objects.get_or_create(label=item.category)
		i.category = category

		subcategory, created = SubCategory.objects.get_or_create(label=item.subcategory)
		i.subcategory = subcategory

		i.units = item.units
		i.label = item.label
		i.emissionDate = item.emissionDate
		i.expirationDate = item.expirationDate
		i.numberOfCopies = item.numberOfCopies

		i.save()
		
if __name__ == "__main__":
	l = process()
	insert(l)
	