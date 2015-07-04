__author__ = 'plasmashadow'

from stackexchange import Request

class Answer(object):

    route = "answers"

    def get_all_answers(self, **kwargs):
        return Request(self.route, **kwargs).do()

    def get_by_id(self, id, **kwargs):
        _route = self.route+"/"+str(id)
        return Request(_route, **kwargs).do()

    def get_comments(self, id, **kwargs):
         _route = self.route+"/"+str(id)+"/"+"comments"
         return Request(_route, **kwargs).do()

