from collections import abc
from collections import UserDict
from json import loads


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


def test_impl(cls, data):
    data = loads(data)
    feed = cls(data)
    assert len(feed.Schedule.speakers) == 1
    print(sorted(feed.Schedule.keys()))

    for key, value in sorted(feed.Schedule.items()):
        print(f"{len(value)}\t{key}")

    feed.Schedule.speakers[-1].name  # This fails for 'FrozenJSON'

    talk = feed.Schedule.events[0]
    assert talk.name

    try:
        talk.flavor
    except AttributeError as e:
        print("Got the correct attribute error!")
    except KeyError as e:
        print("Got a KeyError")


data = """
{
    "Schedule": {
        "conferences": [
            {
                "serial": 115
            }
        ],
        "events": [
            {
                "serial": 34505,
                "name": "Why Schools Don't Use Open Source to Teach Programming",
                "event_type": "40-minute conference session",
                "time_start": "2014-07-23 11:30:00",
                "time_stop": "2014-07-23 12:10:00",
                "venue_serial": 1462,
                "description": "Aside from the fact that high school programming...",
                "website_url": "http://oscon.com/oscon2014/public/schedule/detail/34505",
                "speakers": [
                    157509
                ],
                "categories": [
                    "Education"
                ]
            }
        ],
        "speakers": [
            {
                "serial": 157509,
                "name": "Robert Lefkowitz",
                "photo": null,
                "url": "http://sharewave.com/",
                "position": "CTO",
                "affiliation": "Sharewave",
                "twitter": "sharewaveteam",
                "bio": "Robert 'r0ml' Lefkowitz is the CTO at Sharewave, a startup..."
            }
        ],
        "venues": [
            {
                "serial": 1462,
                "name": "F151",
                "category": "Conference Venues"
            }
        ]
    }
}
"""


class FrozenJSON(UserDict):
    """
    Attemptful reimplementation of Ramalho's FrozenJSON - no peeking!
    """

    def __init__(self, data):
        self.data = data
        for key, val in data.items():
            if isinstance(val, dict):
                val = FrozenJSON(val)

            self.__setattr__(key, val)


class FrozenJSON2:
    """
    Ramalho's FrozenJSON
    """

    def __init__(self, data):
        self.__data = dict(data)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        return FrozenJSON2.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)

        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


test_impl(FrozenJSON2, data)

class FrozenJSON3:
    """
    Ramalho's FrozenJSON with AttributeError handling
    """

    def __init__(self, data):
        self.__data = dict(data)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        elif name in self.__data:
            return FrozenJSON3.build(self.__data[name])
        else:
            raise AttributeError(f"Attribute {name} not found")

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)

        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

test_impl(FrozenJSON3, data)