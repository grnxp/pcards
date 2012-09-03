from cards.models import *
from django.contrib import admin
from xcards.autocomplete.widgets import *

admin.site.register(Country)
admin.site.register(Tag)

class CardAdmin(AutocompleteModelAdmin):
	related_search_fields = {
		'country' : ('label',),
		'tags' : ('label',),
	}

admin.site.register(Card, CardAdmin)
