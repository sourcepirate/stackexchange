__author__ = 'plasmashadow'

import unittest
from stackexchange.api._api_response import _response

class TestResponse(unittest.TestCase):

    def test_response(self):
        res = _response([{'a': 3, 'b': 4, 'g': {'c': 45}}])
        self.assertEqual(res.results[0].g.c, 45)