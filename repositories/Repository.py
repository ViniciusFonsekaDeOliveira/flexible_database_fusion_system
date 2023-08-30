from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def findAll(self, *args):
        pass

    @abstractmethod
    def findOneByData(self, *args):
        pass

    @abstractmethod
    def insert(self, *args):
        pass

    @abstractmethod
    def update(self, *args):
        pass

    @abstractmethod
    def delete(self, *args):
        pass
