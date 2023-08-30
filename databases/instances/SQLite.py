from databases.connection.SqliteDatabase import SQLiteDatabase


class SQLite:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SQLite, cls).__new__(cls)
            cls._instance.db_instance = SQLiteDatabase(
                host=None,
                port=None,
                user=None,
                password=None,
                database_name="mySqlite_db.db"
            )
