__author__ = 'plasmashadow'

from ._api_request import _request
from ._api_base import _get, _post, _build_path
from ._api_reader import *

class Request(_request):
    """
      Request Object is the Essential Object for all stackexchange
      Api request

      >>> r = Request("route", {'site': 'stackoverflow'})
      >>> g = r.do()

      When Specifing date specify the unix timestamp
    """
    pass

build_sub_path = _build_path


