from adapters.RelationalAdapter import RelationalAdapter


class SQLiteStrategy(RelationalAdapter):
    def __init__(self, sqlitedb_instance):
        self._sqlitedb = sqlitedb_instance

    @property
    def sqlitedb(self):
        return self._sqlitedb

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
