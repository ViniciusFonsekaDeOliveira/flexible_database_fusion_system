from adapters.RelationalAdapter import RelationalAdapter


class PostgresStrategy(RelationalAdapter):
    def __init__(self, postgresdb_instance):
        self._postgresdb = postgresdb_instance

    @property
    def postgresdb(self):
        return self._postgresdb

   # TO DO: especific CRUD operations related to postgres database
