from adapters.RelationalAdapter import RelationalAdapter


class SQLServerStrategy(RelationalAdapter):
    def __init__(self, sqlserver_instance):
        self._sqlserver = sqlserver_instance

    @property
    def sqlserver(self):
        return self._sqlserver

   # TO DO: especific CRUD operations related to SQL Server database
