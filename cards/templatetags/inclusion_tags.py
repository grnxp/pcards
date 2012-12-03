from django import template
from django.conf import settings
from cards.models import Country, Category, Card

register = template.Library()

def nav_menu():
	countries = Country.objects.all().order_by('label')
	return { 'countries' : countries }
	
def cards_list_partial(cardslist):
	return { 'cards_list': cardslist }
	
def random_pics():
	return { 'random_pics': Card.objects.order_by('?')[:15] }

register.inclusion_tag('nav_menu.html')(nav_menu)
register.inclusion_tag('cards_list.html')(cards_list_partial)
register.inclusion_tag('random_pics.html')(random_pics)
