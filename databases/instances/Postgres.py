from databases.connection.PostgresDatabase import PostgresDatabase


class Postgres:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Postgres, cls).__new__(cls)
            cls._instance.db_instance = PostgresDatabase(
                host="localhost",
                port=5432,
                user="postgres",
                password="example",
                database_name="myPostgres_db"
            )
        return cls._instance
