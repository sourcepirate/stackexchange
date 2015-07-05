__author__ = 'plasmashadow'

from stackexchange import Request, build_sub_path

class Question(object):

    route = "questions"

    def get_all_question(self, **kwargs):
        return Request(self.route, **kwargs).do()

    def get_by_id(self, id, **kwargs):
        _route = self.route+"/"+str(id)
        return Request(_route, **kwargs).do()

    def get_answer(self, id, **kwargs):
        _route = self.route+"/"+str(id)+"/answers"
        return Request(_route, **kwargs).do()

    def get_comments(self, id, **kwargs):
        _route = self.route+"/"+str(id)+"/comments"
        return Request(_route, **kwargs).do()

    def get_unanswered(self, **kwargs):
        _route = build_sub_path([self.route, "unanswered"])
        return Request(_route, **kwargs).do()

    def get_featured(self, **kwargs):
        _route = build_sub_path([self.route, "featured"])
        return Request(_route, **kwargs).do()

