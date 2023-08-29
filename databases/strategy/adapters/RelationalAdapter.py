from abc import ABC, abstractmethod


class RelationalAdapter(ABC):
    @abstractmethod
    def findAll(self, connection, cursor, table: str, field: str = "*"):
        pass

    @abstractmethod
    def findOneByData(self, connection, cursor, table: str, dataToSearch: dict, fields: str = "*"):
        pass

    @abstractmethod
    def insert(self, connection, cursor, table: str, dataToInsert: dict):
        pass

    @abstractmethod
    def update(self, connection, cursor, table: str, dataIdentifier: dict, updatedData: dict):
        pass

    @abstractmethod
    def delete(self, connection, cursor, table: str, dataIdentifier: dict):
        pass
