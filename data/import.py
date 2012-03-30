#coding=utf-8

from lxml import etree
import os

def process():
	"""
	Ouvre un fichier GCStar structuré de la manière suivante:
	
		<collection...>
			 <item
			  gcsfield1="France" => pays
			  gcsfield2="1" => avec ou sans puce
			  gcsfield3="france/Alimentation/Gourmandises/milka 50.jpg" => image
			  gcsfield4="Gourmandises" => souscatégorie
			  gcsfield5="50" => unités
			  gcsfield6="Milka Lila Pause" => label
			  gcsfield7="02/1996" => année d'émission
			  gcsfield8="" => date d'expiration
			  gcsfield9="B61013013" => pas utile
			  gcsfield10="1000000" => tirage
			  gcsfield11="Alimentation " => catégorie
			  gcsautoid="19" => nafout
			 >
		</collection>
	"""
	a = r'collection.gcs'
	element = etree.parse(a)
	items = element.xpath('//collection/item')
	
	for item in items:
		print item
	
if __name__ == "__main__":
	process()