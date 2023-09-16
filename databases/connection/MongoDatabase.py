from pymongo import MongoClient
from urllib.parse import quote_plus
from DatabaseConnection import DatabaseConnection


class MongoDatabase(DatabaseConnection):
    def connect(self):
        client = MongoClient(self.host)  # "mongodb://localhost:27017/"
        return client[self.database_name]

    @property
    def connection_string(self):
        uri = "mongodb://%s:%s@%s" % (quote_plus(self.user),
                                      quote_plus(self.password), self.host)
        return uri
