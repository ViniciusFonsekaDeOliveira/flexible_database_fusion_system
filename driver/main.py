from databases.factory.DatabaseFactory import DatabaseFactory
from databases.strategy.MysqlStrategy import MySQLStrategy
from databases.strategy.PostgresStrategy import PostgresStrategy
from databases.strategy.SQLiteStrategy import SQLiteStrategy
from databases.strategy.SqlServerStrategy import SQLServerStrategy
from databases.strategy.MongoStrategy import MongoStrategy
from repositories.PersonRepository import PersonRepository


if __name__ == "__main__":

    mysql = "mysql"
    postgres = "postgres"
    sqlite = "sqlite"
    sqlserver = "sqlserver"
    mongo = "mongodb"

    mysql_connection = {
        "host": "test",
        "port": "test",
        "user": "test",
        "password": "test",
        "database": "test"
    }
    postgres_connection = {}
    sqlite_connection = {}
    sqlserver_connection = {}
    mongodb_connection = {}

    db_instance = DatabaseFactory.create_database_connection(
        mysql, **mysql_connection)

    mysql_strategy = MySQLStrategy(db_instance)
    postgres_strategy = PostgresStrategy(db_instance)
    sqlite_strategy = SQLiteStrategy(db_instance)
    sqlserver_strategy = SQLServerStrategy(db_instance)
    mongo_strategy = MongoStrategy(db_instance)

    # Use case
    personRepository = PersonRepository(mysql_strategy)
