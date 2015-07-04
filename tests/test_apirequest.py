__author__ = 'plasmashadow'

import unittest



class TestRequest(unittest.TestCase):

    def test_request_hey(self):
        g = Request("answers", order="desc", sort="activity", site="stackoverflow")
        res = g.do()
        self.assertEqual(res.results[0].is_accepted, False)