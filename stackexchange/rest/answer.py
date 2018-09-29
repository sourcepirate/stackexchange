__author__ = 'plasmashadow'

from stackexchange import Request

class Answer(object):

    def __init__(self, site, **kwargs):
        self.__dict__.update(kwargs)
        self.site = site

    route = "answers"

    def get_all_answers(self, **kwargs):
        kwargs["site"] = self.site
        return Request(self.route, **kwargs).do()

    def get_by_id(self, id, **kwargs):
        kwargs["site"] = self.site
        _route = self.route+"/"+str(id)
        return Request(_route, **kwargs).do()

    def get_comments(self, id, **kwargs):
        kwargs["site"] = self.site
        _route = self.route+"/"+str(id)+"/"+"comments"
        return Request(_route, **kwargs).do()

