from databases.connection.MysqlDatabase import MysqlDatabase


class MySQL:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MySQL, cls).__new__(cls)
            cls._instance.db_instance = MysqlDatabase(
                host="localhost",
                port="3306",
                user="root",
                password="example",
                database_name="mysql_db"
            )
        return cls._instace
