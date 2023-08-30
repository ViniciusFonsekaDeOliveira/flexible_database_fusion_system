from databases.connection.MysqlDatabase import MysqlDatabase


class MySQL:
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            cls._instance = super(MySQL, cls).__new__(cls, **kwargs)
            cls._instance.db_instance = MysqlDatabase(**kwargs)
        return cls._instace
