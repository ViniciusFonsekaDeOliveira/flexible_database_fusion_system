from adapters.RelationalAdapter import RelationalAdapter


class MySQLStrategy(RelationalAdapter):
    def __init__(self, mysqldb_instace):
        self._mysqldb = mysqldb_instace

    @property
    def mysqldb(self):
        return self._mysqldb

    # TO DO: especific CRUD operations to mysql databases
