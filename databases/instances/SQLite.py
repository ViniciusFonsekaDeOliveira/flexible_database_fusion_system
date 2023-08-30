from databases.connection.SqliteDatabase import SQLiteDatabase


class SQLite:
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            cls._instance = super(SQLite, cls).__new__(cls, **kwargs)
            cls._instance.db_instance = SQLiteDatabase(**kwargs)
        return cls._instance
