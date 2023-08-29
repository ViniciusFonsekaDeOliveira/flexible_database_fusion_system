import mysql.connector as mysql
from DatabaseConnection import DatabaseConnection


class MysqlDatabase(DatabaseConnection):
    def connect(self):
        return mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database_name
        )
