__author__ = 'plasmashadow'

from stackexchange import Request, build_sub_path

class Question(object):

    def __init__(self, site, **kwargs):
        self.__dict__.update(kwargs)
        self.site = site

    route = "questions"

    def get_all_questions(self, **kwargs):
        kwargs["site"] = self.site
        return Request(self.route, **kwargs).do()

    def get_by_id(self, id, **kwargs):
        _route = self.route+"/"+str(id)
        kwargs["site"] = self.site
        return Request(_route, **kwargs).do()

    def get_answer(self, id, **kwargs):
        _route = self.route+"/"+str(id)+"/answers"
        kwargs["site"] = self.site
        return Request(_route, **kwargs).do()

    def get_comments(self, id, **kwargs):
        _route = self.route+"/"+str(id)+"/comments"
        kwargs["site"] = self.site
        return Request(_route, **kwargs).do()

    def get_unanswered(self, **kwargs):
        _route = build_sub_path([self.route, "unanswered"])
        kwargs["site"] = self.site
        return Request(_route, **kwargs).do()

    def get_featured(self, **kwargs):
        _route = build_sub_path([self.route, "featured"])
        kwargs["site"] = self.site
        return Request(_route, **kwargs).do()

