import psycopg2 as postgres
from DatabaseConnection import DatabaseConnection


class PostgresDatabase(DatabaseConnection):
    def connect(self):
        return postgres.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database_name
        )
