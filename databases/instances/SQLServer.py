from databases.connection.SQLServerDatabase import SQLServerDatabase


class SQLServer:
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            cls._instance = super(SQLServer, cls).__new__(cls, **kwargs)
            cls._instance.db_instance = SQLServerDatabase(**kwargs)
        return cls._instance
