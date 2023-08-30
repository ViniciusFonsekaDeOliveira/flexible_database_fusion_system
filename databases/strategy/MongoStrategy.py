from adapters.NoRelationalAdapter import NoRelationalAdapter


class MongoStrategy(NoRelationalAdapter):
    def __init__(self, mongodb_instance):
        self._mongodb = mongodb_instance

    @property
    def mongodb(self):
        return self._mongodb
