__author__ = 'plasmashadow'

import unittest
from stackexchange.api import Request


class TestRequest(unittest.TestCase):

    def test_request_hey(self):
        g = Request("answers", order="desc", sort="activity", site="stackoverflow")
        res = g.do()
        self.assertIsNotNone(res)