from lxml import etree
import os

def process():
	a = r'collection.gcs'
	element = etree.parse(a)
	items = element.xpath('//Collection')
	
	for item in items:
		print item
	
if __name__ == "__main__":
	process()