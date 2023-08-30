from databases.connection.MongoDatabase import MongoDatabase


class Mongo:
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            cls._instance = super(Mongo, cls).__new__(cls, **kwargs)
            cls._instance.db_instance = MongoDatabase(**kwargs)
        return cls._instance
