# coding: utf-8


class HashTable:

    def __init__(self):
        self._table = [[] for _ in range(1000)]


    @staticmethod
    def hash(string):
        return len(string)

    def append(self, string):
       self._table[self.hash(string) % 1000].append(string)

    def search(self, string):
        sublist = self._table[self.hash(string)]
        return string in sublist

