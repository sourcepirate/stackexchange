__author__ = 'plasmashadow'

import six
import urllib
import requests


class _object(object):
    pass

def _transform_to_object(item):

    custom_obj = _object()
    for key, value in six.iteritems(item):

        if isinstance(value, dict):
            custom_obj.__dict__.update({key: _transform_to_object(item)})
        elif isinstance(value, list)
            custom_obj.__dict__.update({key: value})
        else:
            custom_obj.__dict__.update({key: value})

    return custom_obj

def _construct_url(route, version, **kwargs):

    version = version or "2.2"
    host = "https://api.stackexchange.com/"+version+"/"+route+"?"+urllib.urlencode(**kwargs)
    return host

def _get(url, *args, **kwargs):
    return requests.get(url).content

def _post(url, *args, **kwargs):
    return requests.post(url).content
