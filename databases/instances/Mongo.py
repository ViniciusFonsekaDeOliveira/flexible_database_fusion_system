from databases.connection.MongoDatabase import MongoDatabase


class Mongo:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Mongo, cls).__new__(cls)
            cls._instance.db_instance = MongoDatabase(
                host="localhost",
                port=27017,
                user=None,
                password=None,
                database_name="mydb")
            return cls._instance
