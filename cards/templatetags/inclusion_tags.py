from django import template
from django.conf import settings
from cards.models import Country, Category

register = template.Library()

def nav_menu():
	categories = Category.objects.all().order_by('label')
	countries = Country.objects.all().order_by('label')
	return { 'countries' : countries, 'categories' : categories }

register.inclusion_tag('nav_menu.html')(nav_menu)