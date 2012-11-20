#coding=utf-8

from cards.models import *
from django.contrib import admin
from xcards.autocomplete.widgets import *
import os
from cards.templatetags.image_tags import scale


class CardInline(admin.StackedInline):
	model = Card
	
class CardForTagInline(admin.StackedInline):
	model = Card.tags.through
	
	search_fields = ['label',]
	
class TagAdmin(admin.ModelAdmin):
	inlines = [CardForTagInline,]
	
	search_fields = ['label',]
	
class CountryAdmin(admin.ModelAdmin):
	inlines = [CardInline,]
	
	search_fields = ['label',]

class CardAdmin(AutocompleteModelAdmin):
	### à checker par la suite, gros gros bug prévu, tout ça...
	related_search_fields = {
		'tags' : ('label',),
	}
	
	list_filter = ('country__label', 'tags__label')
	list_display = ('thumbnail', 'label', 'Pays')
	raw_id_admin = ('country',)
	
	def Pays(self, obj):
		return obj.country.label
		
	def thumbnail(self, obj):
		if obj.image:
			return u'<img src="%s" />' % (scale(obj, 'tiny'))
		else:
			return '(pas d''image)'
			
	thumbnail.short_description = 'Thumb'
	thumbnail.allow_tags = True
	
	date_hierarchy = 'created_at'
	
admin.site.register(Country, CountryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Card, CardAdmin)
