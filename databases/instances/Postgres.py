from databases.connection.PostgresDatabase import PostgresDatabase


class Postgres:
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            cls._instance = super(Postgres, cls).__new__(cls, **kwargs)
            cls._instance.db_instance = PostgresDatabase(**kwargs)
        return cls._instance
