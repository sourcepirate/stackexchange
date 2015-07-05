__author__ = 'plasmashadow'

import six
import urllib
import json
import requests


class _object(object):
    pass

def _transform_to_object(item):
    """
      Creates an Object from its dict or list item.
      So that we don't have access it through its square brackets.
    :param item:
    :return:
    """
    custom_obj = _object()
    for key, value in six.iteritems(item):

        if isinstance(value, dict):
            custom_obj.__dict__.update({key: _transform_to_object(value)})
        elif isinstance(value, list):
            custom_obj.__dict__.update({key: value})
        else:
            custom_obj.__dict__.update({key: value})

    return custom_obj

def _construct_url(route, version, **kwargs):
    """
     Used to create a Route url for app exchange.
    :param route:
    :param version:
    :param kwargs:
    :return:
    """
    version = version or "2.2"
    host = "https://api.stackexchange.com/"+version+"/"+route+"?"+urllib.urlencode(kwargs)
    return host

def parse(func):
    """
      a decorater used to convert the response to Object
    :param func:
    :return:
    """
    def inner(url, *args, **kwargs):
        data = func(url, *args, **kwargs)
        data = json.loads(data)
        _results = []
        for item in data["items"]:
            _results.append(_transform_to_object(item))
        return _results
    return inner

@parse
def _get(url, *args, **kwargs):
    return requests.get(url).content
@parse
def _post(url, *args, **kwargs):
    return requests.post(url).content


def _build_path(*args):
    _route = ""
    for key in args:
        _route = _route+"/"+str(key)
    return _route
