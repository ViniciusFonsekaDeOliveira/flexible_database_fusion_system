from abc import ABC, abstractmethod


class RelationalAdapter(ABC):
    @abstractmethod
    def findAll(self, table: str, fields: str = "*"):
        pass

    @abstractmethod
    def findOneByData(self, table: str, dataToSearch: dict, fields: str = "*"):
        pass

    @abstractmethod
    def insert(self, table: str, dataToInsert: dict):
        pass

    @abstractmethod
    def update(self, table: str, dataIdentifier: dict, updatedData: dict):
        pass

    @abstractmethod
    def delete(self, table: str, dataIdentifier: dict):
        pass
