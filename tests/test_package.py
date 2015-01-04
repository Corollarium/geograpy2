# -*- coding: utf-8 -*-

import unittest
import geograpy2

class TestExtractor(unittest.TestCase):
    def test_italy(self):
        text = u"""Qualsiasi cosa qui. Via Alberto da Padova, 232 - Padova Italy"""
        places = geograpy2.get_place_context(text=text)
        # TODO self.assert

def main():
    unittest.main()

if __name__ == '__main__':
    main()