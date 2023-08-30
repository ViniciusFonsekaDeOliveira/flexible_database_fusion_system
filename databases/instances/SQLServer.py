from databases.connection.SQLServerDatabase import SQLServerDatabase


class SQLServer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SQLServer, cls).__new__(cls)
            cls._instance.db_instance = SQLServerDatabase(
                host="localhost",
                port=1433,
                user="user",
                password="password",
                database_name="mySQLServer_db"
            )
        return cls._instance
