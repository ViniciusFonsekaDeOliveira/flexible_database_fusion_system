from abc import ABC, abstractmethod


class NoRelationalAdapter(ABC):
    @abstractmethod
    def findAll(self, collection_name, fields: dict = None):
        pass

    @abstractmethod
    def findOneByData(self, collection_name: str, dataToSearch: dict, fields: dict = None):
        pass

    @abstractmethod
    def insert(self, collection_name: str, dataToInsert: dict):
        pass

    @abstractmethod
    def update(self, collection_name: str, dataIdentifier: dict, updatedData: dict):
        pass

    @abstractmethod
    def delete(self, collection_name: str, dataIdentifier: dict):
        pass
