# Create your views here.
#coding utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django import forms
from cards.models import Item, Country, Category, SubCategory
from django.core.context_processors import csrf

def index(request):
	cards_list = Item.objects.order_by('-created_at')[:21]
	
	context = { 'cards_list' : cards_list}

	return render_to_response('cards/index.html', RequestContext(request, context))
	
def details(request, item_id):
	a = get_object_or_404(Item, pk=item_id)
	
	context = {'card': a }	

	return render_to_response('cards/details.html', RequestContext(request, context))
	
def search_by_country(request, country_id, page_number):
	country = get_object_or_404(Country, pk=country_id)
	
	context = { 'object' : country }
	
	return render_to_response('cards/list.html', RequestContext(request, context))

def search_by_category(request, category_id, page_number):
	country = get_object_or_404(Category, pk=category_id)
	
	context = { 'object' : country }
	
	return render_to_response('cards/list.html', RequestContext(request, context))
	
def search_by_subcategory(request, subcategory_id, page_number):
	country = get_object_or_404(SubCategory, pk=subcategory_id)
	
	context = { 'object' : country }
	
	return render_to_response('cards/list.html', RequestContext(request, context))