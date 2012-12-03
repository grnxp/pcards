# Create your views here.
#coding=utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django import forms
from cards.models import Card, Country, Tag
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import cards.forms

def index(request):
	from django.db.models import Count
	
	nbr_of_cards = Card.objects.count()
	
	tags_list = Tag.objects.order_by('?').annotate(occurences=Count('tags'))[:25]
	
	cards_list = Card.objects.order_by('-created_at')[:25]
	
	context = { 'tags_list' : tags_list,'cards_list' : cards_list}

	return render_to_response('cards/index.html', RequestContext(request, context))
	
def about(request):
	return render_to_response('cards/about.html', RequestContext(request, {}))
	
def tags(request):
	from django.db.models import Count
	
	tags_list = Tag.objects.annotate(occurences=Count('tags'))
	
	context = { 'tags_list' : tags_list }
	
	return render_to_response('cards/tags.html', RequestContext(request, context))
	
def details(request, card_id):
	a = get_object_or_404(Card, pk=card_id)
	
	context = {'card': a }	

	return render_to_response('cards/details.html', RequestContext(request, context))
	
def charts(request):
	from django.db.models import Count
	
	c = Country.objects.annotate(num_cards=Count('card'))
	
	context = {'countries': c, 'c_string': ', '.join(("'" + x.label + "'" for x in c)) }
	
	return render_to_response('cards/charts.html', RequestContext(request, context))

def query(request):
	
	if request.method == "POST":
		terms = request.POST['q']
		#request.POST.urlencode()
		
	else:
		terms = request.GET['q']
	
	from django.db.models import Q
	
	q = Q()
	t = Q()
	
	for term in terms.split(' '):
		q.add((Q(label__icontains=term) | Q(country__label__icontains=term) ), q.AND)
		t.add((Q(label__icontains=term)), t.AND)
	
	tags_list = Tag.objects.filter(t)
	
	cards_list = Card.objects.filter(q)
		
	cards = cards_list
	
	context = { 'tags_list': tags_list, 'cards' : cards, 'title' : 'Recherche sur les termes : ' + terms }
	
	return render_to_response('cards/list.html', RequestContext(request, context))

def advanced_query(request):
	if request.method == 'POST':
		form = cards.forms.AdvancedQueryForm(request.POST)
		
		if form.is_valid():
			print 'form is valid'
			
			from django.db.models import Q
			
			q = Q()
			
			# le label d'abord...
			for term in form.label.split(' '):
				q.add(Q(label__icontains=term), q.OR)
				
			# le ou les pays
			for term in form.country.split(' '):
				q.add(Q(country__label__icontains=term), q.OR)
				
			# avec puce ou sans puce (ou sans rien...)
			if form.with_chip is not 'Unknown':
				if form.with_chip == 'True':
					q.add(Q(with_chip__isTrue), q.AND)
				else:
					q.add(Q(with_chip__isNotTrue), q.AND)
			
			# la date de début
			# faut modifier le modèle ici...
				
			cards_list = Card.objects.filter(q)
			
			cards_list = pagination(cards_list, request)
			
			context = { 'cards' : cards_list, 'title' : 'Recherche avancée' }
			
			return render_to_response('cards/list.html', RequestContext(request, context))
	
	else:
		form = cards.forms.AdvancedQueryForm()

	context = { 'form' : form }
	
	return render_to_response('cards/advanced_query.html', RequestContext(request, context)) 

def search_by_country(request, country_id):
	country = get_object_or_404(Country, pk=country_id)
	
	cards = country.card_set.all()
	
	context = { 'cards' : cards, 'title' : country.label }
	
	return render_to_response('cards/list.html', RequestContext(request, context))

def search_by_tag(request, tag_id):
	tag = get_object_or_404(Tag, pk=tag_id)
	
	cards_list = tag.tags.all()
	
	cards = cards_list
	
	context = { 'cards' : cards, 'title' : tag.label }
	
	return render_to_response('cards/list.html', RequestContext(request, context))

