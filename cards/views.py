# Create your views here.
#coding utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django import forms
from cards.models import Item, Country, Category, SubCategory
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	cards_list = Item.objects.order_by('-created_at')[:25]
	
	context = { 'cards_list' : cards_list}

	return render_to_response('cards/index.html', RequestContext(request, context))
	
def details(request, item_id):
	a = get_object_or_404(Item, pk=item_id)
	
	context = {'card': a }	

	return render_to_response('cards/details.html', RequestContext(request, context))

def pagination(cards_list, request):
	paginator = Paginator(cards_list, 25)
	
	page = request.GET.get('page')
	
	try:
		cards = paginator.page(page)
	except PageNotAnInteger:
		cards = paginator.page(1)
	except EmptyPage:
		cards = paginator.page(paginator.num_pages)
	
def query(request):
	
	if request.method == "POST":
		terms = request.POST['q']
		
	else:
		terms = request.GET['q']
	
	from django.db.models import Q
	
	q = Q()
	
	for term in terms.split(' '):
		q.add((Q(label__icontains=term) | Q(subcategory__label__icontains=term) | Q(subcategory__category__label__icontains=term) | Q(country__label__icontains=term) ), q.AND)
	
	cards_list = Item.objects.filter(q)
	
	cards = pagination(cards_list, request)
	
	context = { 'cards_list' : cards, 'title' : 'Recherche sur les termes : ' + terms }
	
	return render_to_response('cards/list.html', RequestContext(request, context))

def advanced_query(request):
	context = { }
	
	return render_to_response('cards/advanced_query.html', RequestContext(request, context)) 

def search_by_country(request, country_id):
	country = get_object_or_404(Country, pk=country_id)
	
	cards = pagination(country.item_set.all(), request)
	
	context = { 'cards_list' : cards, 'title' : country.label }
	
	return render_to_response('cards/list.html', RequestContext(request, context))

def search_by_category(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	
	cards_list = list()
	
	for subcat in category.subcategory_set.all():
		cards_list.extend(subcat.item_set.all())
		
	cards = pagination(cards_list, request)
	
	context = { 'cards_list' :  cards, 'title' : category.label }
	
	return render_to_response('cards/list.html', RequestContext(request, context))
	
def search_by_subcategory(request, subcategory_id):
	subcategory = get_object_or_404(SubCategory, pk=subcategory_id)
	
	cards = pagination(subcategory.item_set.all(), request)
	
	context = { 'cards_list' : cards, 'title' : subcategory.label }
	
	return render_to_response('cards/list.html', RequestContext(request, context))
