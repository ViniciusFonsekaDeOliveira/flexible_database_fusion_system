from adapters.NoRelationalAdapter import NoRelationalAdapter


class MongoStrategy(NoRelationalAdapter):
    def __init__(self, mongodb_instance):
        self._mongodb = mongodb_instance

    @property
    def mongodb(self):
        return self._mongodb

    def findAll(self, connection, collection_name):
        pass

    def findOneByData(self, connection, collection_name, query):
        pass

    def insert(self, connection, collection_name, document):
        pass

    def update(self, connection, collection_name, query, updated_data):
        pass

    def delete(self, connection, collection_name, query):
        pass
