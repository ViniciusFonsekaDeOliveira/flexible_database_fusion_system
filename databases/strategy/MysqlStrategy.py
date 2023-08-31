from adapters.RelationalAdapter import RelationalAdapter


class MySQLStrategy(RelationalAdapter):
    def __init__(self, mysqldb_instace):
        self._mysqldb = mysqldb_instace

    @property
    def mysqldb(self):
        return self._mysqldb

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
