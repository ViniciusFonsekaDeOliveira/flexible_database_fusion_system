import sqlite3 as sqlite
from DatabaseConnection import DatabaseConnection


class SQLiteDatabase(DatabaseConnection):
    def connect(self):
        return sqlite.connect(self.database_name)
