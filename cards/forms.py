#coding=utf-8

from django import forms

class AdvancedQueryForm(forms.Form):
	WITH_CHIP_CHOICES = (
		('Unknown', 'Afficher toutes les cartes'),
		('True', 'Seulement les cartes avec puce'),
		('False', 'Seulement les cartes sans puce'),
	)

	label = forms.CharField(max_length=100, label='Label')
	country = forms.CharField(max_length=100, label='Pays')
	with_chip = forms.ChoiceField(label='Puce', choices=WITH_CHIP_CHOICES)
	year_begin = forms.IntegerField(label='Date de début')
	year_end = forms.IntegerField(label='Date de fin')
