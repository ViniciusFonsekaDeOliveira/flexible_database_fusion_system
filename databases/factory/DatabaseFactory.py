from instances.SQLite import SQLite
from instances.MySQL import MySQL
from instances.Postgres import Postgres
from instances.SQLServer import SQLServer
from instances.Mongo import Mongo


class DatabaseFactory:
    @staticmethod
    def create_database_connection(self, db_type: str, **kwargs):
        if db_type == "sqlite":
            return SQLite(**kwargs)
        elif db_type == "mysql":
            return MySQL(**kwargs)
        elif db_type == "postgres":
            return Postgres(**kwargs)
        elif db_type == "sqlserver":
            return SQLServer(**kwargs)
        elif db_type == "mongodb":
            return Mongo(**kwargs)
        else:
            print("Invalid database option!")
