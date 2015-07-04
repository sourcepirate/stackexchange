__author__ = 'plasmashadow'

from ._api_base import _get, _post, _construct_url

class _request(object):

    def __init__(self, route, **kwargs):
        self.url = _construct_url(route, kwargs.pop("version", "2.2"), **kwargs)

    def do(self):
        return _get(self.url)
