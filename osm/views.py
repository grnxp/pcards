# Create your views here.

#coding=utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django import forms
from cards.models import Card, Country, Category, SubCategory
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from osm.models import Coordinates

def map(request):
	coordinates = Coordinates.objects.all()
	
	context = { 'coordinates' : coordinates }
	
	return render_to_response('osm/map.html', RequestContext(request, context))
