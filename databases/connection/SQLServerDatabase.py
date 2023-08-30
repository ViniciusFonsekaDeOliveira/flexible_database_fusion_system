import pyodbc as sql_server
from DatabaseConnection import DatabaseConnection


class SQLServerDatabase(DatabaseConnection):
    def connect(self):
        return sql_server.connect(self.connection_string)

    @property
    def connection_string(self):
        return (
            f"DRIVER=OBBC Driver 17 for SQL Server;"
            f"SERVER={self.host}, {self.port};"
            f"DATABASE={self.database_name};"
            f"UID={self.user}"
            f"PWD={self.password}"
        )
