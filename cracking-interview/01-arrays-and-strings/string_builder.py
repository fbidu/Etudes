# coding: utf-8


class StringBuilder:

    def __init__(self, string=None):
        self._sentence = []
        if string:
            self._sentence.append(string)

    def append(self, string):
        self._sentence.append(string)

    def __str__(self):
        return ''.join(self._sentence)

