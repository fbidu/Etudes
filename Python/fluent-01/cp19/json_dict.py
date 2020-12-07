from json import load, loads


class JSONDict:
    """
    First interaction of a 'json dict'

    >>> a = JSONDict('{"name": "potato", "tasty": 2, "earthy": true}')
    >>> a.name
    'potato'
    >>> a.tasty
    2
    >>> a.earthy
    True
    """

    def __init__(self, json):
        json_data = loads(json)

        for key, value in json_data.items():
            self.__setattr__(key, value)
