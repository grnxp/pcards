#coding=utf-8

from django.utils import unittest
from cards.management.commands import gcstar_import

class ImportTestCase(unittest.TestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_get_absfilepath(self):
		self.assertEqual(1, 2)
