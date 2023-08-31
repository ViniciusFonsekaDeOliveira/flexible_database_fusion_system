from adapters.RelationalAdapter import RelationalAdapter


class PostgresStrategy(RelationalAdapter):
    def __init__(self, postgresdb_instance):
        self._postgresdb = postgresdb_instance

    @property
    def postgresdb(self):
        return self._postgresdb

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
