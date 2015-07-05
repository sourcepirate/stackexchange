__author__ = 'plasmashadow'

import unittest
from stackexchange import search


class TestSearch(unittest.TestCase):

    def test_search(self):
        g = search("python", site="stackoverflow", order="desc")
        self.assertIsNotNone(g)
