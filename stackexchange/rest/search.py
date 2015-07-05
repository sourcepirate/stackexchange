__author__ = 'plasmashadow'


from stackexchange import Request

def search(title, **kwargs):
    """
       Searches for the specified keyword in a site
    :param title:
    :param kwargs:
    :return:
    """
    _route = "search"
    kwargs["intitle"] = title
    return Request(_route, **kwargs).do()

