from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def findAll(self, *args):
        pass

    @abstractmethod
    def find_by_id(self, *args):
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
