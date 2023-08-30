from pymongo import MongoClient
from DatabaseConnection import DatabaseConnection


class MongoDatabase(DatabaseConnection):
    def connect(self):
        client = MongoClient(self.host)
        return client(self.database_name)

    def get_connection_string(self):
        return f"mongodb://{self.user}:{self.password}@{self.host}"
