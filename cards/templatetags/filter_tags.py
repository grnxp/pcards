from django import template
from django.conf import settings
from cards.models import Country, Category

register = template.Library()

def get_range(value):
	"""
		See http://djangosnippets.org/snippets/1357/
		
		Filter - returns a list containing range made from given value
		Usage (in template):

		<ul>{% for i in 3|get_range %}
		  <li>{{ i }}. Do something</li>
		{% endfor %}</ul>

		Results with the HTML:
		<ul>
		  <li>0. Do something</li>
		  <li>1. Do something</li>
		  <li>2. Do something</li>
		</ul>

		Instead of 3 one may use the variable set in the views
	"""
	return range(1, value + 1 )

register.filter(get_range)