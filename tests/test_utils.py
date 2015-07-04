__author__ = 'plasmashadow'


import unittest
import six

from stackexchange.api._api_base import  _transform_to_object


class TestUtils(unittest.TestCase):

    def test_convert_to_object_1(self):
        obj = _transform_to_object({'a': 1, 'b': 2, 'c': {'g': 4}})
        self.assertEqual(obj.c.g, 4)

    def test_convert_to_object_2(self):
        obj = _transform_to_object({'a': 1, 'b': 2, 'c': [1, 2, 3]})
        self.assertEqual(obj.c, [1, 2, 3])

