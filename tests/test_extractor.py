# -*- coding: utf-8 -*-

import unittest
from geograpy2.extraction import Extractor

class TestExtractor(unittest.TestCase):
    def testBBCNews(self):
        e = Extractor(url='http://www.bbc.com/news/world-europe-26919928')
        e.find_entities()
     
        self.assertLess(0, len(e.places))
        self.assertIn('Russia', e.places)
        self.assertIn('Kiev', e.places)
     
    def testNairobi(self):
        text = """ Perfect just Perfect! It's a perfect storm for Nairobi on a 
        Friday evening! horrible traffic here is your cue to become worse @Ma3Route """
     
        e = Extractor(text=text)
        e.find_entities()
     
        self.assertLess(0, len(e.places))
        assert 'Nairobi' in e.places
 
    def testNairobi2(self):
        text3 = """ Risks of Cycling in Nairobi:http://www.globalsiteplans.com/environmental-design/engineering-environmental-design/the-risky-affair-of-cycling-in-nairobi-kenya/ ... via @ConstantCap @KideroEvans @county_nairobi @NrbCity_Traffic """
        e = Extractor(text=text3)
        e.find_entities()
     
        self.assertLess(0, len(e.places))
        self.assertIn('Nairobi', e.places)
 
    def testNairobi3(self):
        text4 = """ @DurbanSharks [Africa Renewal]It is early morning in Nairobi, the Kenyan capital. The traffic jam along Ngong """
        e = Extractor(text=text4)
        e.find_entities()
 
        self.assertLess(0, len(e.places))
        self.assertIn('Nairobi', e.places)
        self.assertIn('Ngong', e.places)
 
    def testNewYork(self):
        # unicode
        text5 = u""" There is a city called New York in the United States."""
        e = Extractor(text=text5)
        e.find_entities()
 
        self.assertEqual(2, len(e.places))
        assert u'New York' in e.places
        assert u'United States' in e.places
 
    def testSaoPaulo(self):
        # unicode and two words
        text6 = u""" There is a city called São Paulo in Brazil."""
        e = Extractor(text=text6)
        e.find_entities()
 
        self.assertEqual(2, len(e.places))
        self.assertIn(u'São Paulo', e.places)
        self.assertIn(u'Brazil', e.places)
         
#     def testSaoPauloPT(self):
#         # Portuguese, unicode and two words
#         text6 = u"""Há uma cidade chamada São Paulo no Brasil."""
#         e = Extractor(text=text6)
#         e.find_entities()
#  
#         self.assertEqual(2, len(e.places))
#         self.assertIn(u'São Paulo', e.places)
#         self.assertIn(u'Brasil', e.places)

def main():
    unittest.main()

if __name__ == '__main__':
    main()