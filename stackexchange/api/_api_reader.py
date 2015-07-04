__author__ = 'plasmashadow'

import requests

def read(url):
    return requests.get(url).content

