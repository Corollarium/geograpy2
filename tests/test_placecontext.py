# -*- coding: utf-8 -*-

import unittest
from geograpy2.placecontext import PlaceContext 

class TestPlaceContext(unittest.TestCase):
    
    def test_sao_paulo_brazil(self):
        pc = PlaceContext([u'São Paulo', 'Brazil'])
    
    def test_Kenya(self):
        pc = PlaceContext(['Ngong', 'Nairobi', 'Kenya'])
        
#         assert len(pc.countries) == 1
#         assert len(pc.cities) == 1
#         assert len(pc.other) == 1
#         assert 'Ngong' in pc.other
#     
#         assert pc.cities_for_name('Nairobi')[0][4] == 'Kenya'
#         assert pc.regions_for_name('Ohio')[0][4] == 'United States'
    
    def test_aleppo(self):
        pc = PlaceContext(['Aleppo', 'Syria'])
    
#         assert 'Aleppo' in pc.cities
        
