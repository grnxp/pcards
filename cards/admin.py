#coding=utf-8

from cards.models import *
from django.contrib import admin
from xcards.autocomplete.widgets import *

admin.site.register(Country)
admin.site.register(Tag)

class CardAdmin(AutocompleteModelAdmin):
	### à checker par la suite, gros gros bug prévu, tout ça...
	related_search_fields = {
		'tags' : ('label',),
	}

admin.site.register(Card, CardAdmin)
