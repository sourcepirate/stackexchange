__author__ = 'plasmashadow'

import unittest
from stackexchange.rest import Answer


class TestAnswer(unittest.TestCase):

    def setUp(self):
        self.answer = Answer()
        self._id_to_find = 31222238

    def test_get_all_answer(self):
        answers = self.answer.get_all_answers(order="desc", sort="activity", site="stackoverflow")
        self.assertIsNotNone(answers)

    def test_get_by_id(self):
        answer = self.answer.get_by_id(self._id_to_find, order="desc", sort="activity", site="stackoverflow")
        self.assertIsNotNone(answer)

    def test_get_all_comments(self):
        answer = self.answer.get_comments(self._id_to_find, site="stackoverflow")
        print answer[0].__dict__
        self.assertIsNotNone(answer)