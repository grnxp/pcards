from django import template
from django.conf import settings
from django.utils.numberformat import format
from osm.models import Coordinates

register = template.Library()

def floatdot(value, separator=".", decimal_pos=4):
	return format(value, separator, decimal_pos)

floatdot.is_safe = True
	
register.filter(floatdot)