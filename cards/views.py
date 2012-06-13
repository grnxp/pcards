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
	
def query(request):
	
	if request.method == "POST":
		terms = request.POST['q']
		
	else:
		terms = request.GET['q']
	
	from django.db import connection
	
	cursor = connection.cursor()
	
	for term in terms.split(' '):
		pass
	
	raw_sql = '%s shalalal %s'
	
	for row in cursor.execute(raw_sql, ['%'+term+'%']):
		print row.id
	
	cards_list = query_set
	
	context = { 'cards_list' : cards_list, 'title' : 'Recherche sur les termes : ' + terms }
	
	return render_to_response('cards/list.html', RequestContext(request, context))

def advanced_query(request):
	return render_to_response('cards/advanced_query.html', RequestContext(request, context)) 

def search_by_country(request, country_id, page_number):
	country = get_object_or_404(Country, pk=country_id)
	
	context = { 'cards_list' : country.item_set.all(), 'title' : country.label }
	
	return render_to_response('cards/list.html', RequestContext(request, context))

def search_by_category(request, category_id, page_number):
	category = get_object_or_404(Category, pk=category_id)
	
	cards_list = list()
	
	for subcat in category.subcategory_set.all():
		cards_list.extend(subcat.item_set.all())
	
	context = { 'cards_list' :  cards_list, 'title' : category.label }
	
	return render_to_response('cards/list.html', RequestContext(request, context))
	
def search_by_subcategory(request, subcategory_id, page_number):
	subcategory = get_object_or_404(SubCategory, pk=subcategory_id)
	
	context = { 'cards_list' : subcategory.item_set.all(), 'title' : subcategory.label }
	
	return render_to_response('cards/list.html', RequestContext(request, context))
	
