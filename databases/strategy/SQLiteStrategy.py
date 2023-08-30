from adapters.RelationalAdapter import RelationalAdapter


class SQLiteStrategy(RelationalAdapter):
    def __init__(self, sqlitedb_instance):
        self._sqlitedb = sqlitedb_instance

    @property
    def sqlitedb(self):
        return self._sqlitedb

    # TO DO: especific CRUD operations realted to sqlite database
