# coding: utf-8
"""
This module defines the ArrayList class. An ArrayList is a list that has a
dynamic size. When you try to insert an item on a full list, it doubles
itself.
It was done just as an exercise suggested by the CtCI book.
In a real world scenario, a normal Python list will do the same trick.
"""
class ArrayList:

    def __init__(self, items=[], size=10):
        self._list = items
        self.size = size
        self.inserted = len(items)

    def append(self, item):
        if self.inserted < self.size:
            self._list.append(item)
        else:
            self = ArrayList(self._list, self.size * 2)
            self.append(item)

    def __str__(self):
        return ', '.join(list(map(str, self._list)))
