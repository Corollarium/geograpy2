# -*- coding: utf-8 -*-

import unittest
from geograpy2.place import Place

class TestPlace(unittest.TestCase):
    def test_basic(self):
        p = Place(city='city', region='region',  country='country')
        self.assertEqual('city', p.city)
        self.assertEqual('region', p.region)
        self.assertEqual('country', p.country)
        