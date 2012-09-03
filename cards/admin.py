from cards.models import *
from django.contrib import admin

admin.site.register(Country)
admin.site.register(Tag)

class CardAdmin(admin.ModelAdmin):
	exclude = ['subcategory']

admin.site.register(Card, CardAdmin)
