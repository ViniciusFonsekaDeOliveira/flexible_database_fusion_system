from adapters.RelationalAdapter import RelationalAdapter


class SQLServerStrategy(RelationalAdapter):
    def __init__(self, sqlserver_instance):
        self._sqlserver = sqlserver_instance

    @property
    def sqlserver(self):
        return self._sqlserver

    def findAll(self, connection, cursor, table: str, field: str = "*"):
        pass

    def findOneByData(self, connection, cursor, table: str, dataToSearch: dict, fields: str = "*"):
        pass

    def insert(self, connection, cursor, table: str, dataToInsert: dict):
        pass

    def update(self, connection, cursor, table: str, dataIdentifier: dict, updatedData: dict):
        pass

    def delete(self, connection, cursor, table: str, dataIdentifier: dict):
        pass
