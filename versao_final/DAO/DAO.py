import json
from abc import ABC
from copy import copy


class DAO(ABC):

    def __init__(self, fonte=''):
        self.fonte = fonte
        self.cache = {}
        try:
            self.__load()
        except TypeError:
            self.__multiple_load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        json.dump(self.cache, open(self.fonte, 'w'), indent=4)

    def __load(self):
        self.cache = json.load(open(self.fonte, 'r'))

    def __multiple_load(self):
        fontes = copy(self.fonte)
        for fonte in fontes:
            self.fonte = fonte
            self.__load()

    def get_all(self):
        return self.cache
