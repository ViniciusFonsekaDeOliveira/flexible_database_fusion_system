from adapters.NoRelationalAdapter import NoRelationalAdapter


class MongoStrategy(NoRelationalAdapter):
    def __init__(self, mongodb_instance):
        self._mongodb = mongodb_instance

    @property
    def connection(self):
        return self._mongodb

    def findAll(self, collection_name: str):
        collection = self.connection[collection_name]
        return list(collection.find())

    # fields = {"nome": 1, "idade": 1, "_id": 0} --> retornará apenas os campos "nome" e "idade", sem incluir o campo "_id" no resultado.
    def findOneByData(self, collection_name: str, dataToSearch: dict, fields: dict = None):
        collection = self.connection[collection_name]
        result = collection.find_one(dataToSearch, fields)
        return result

    def insert(self, collection_name: str, dataToInsert: dict):
        collection = self.connection[collection_name]
        result = collection.insert_one(dataToInsert)
        last_id = result.inserted_id
        return last_id

    def update(self, collection_name: str, dataIdentifier: dict, updatedData: dict):
        collection = self.connection[collection_name]
        # Convertendo o identificador em um formato que o MongoDB compreende
        filter_query = {"$and": [{field: value}
                                 for field, value in dataIdentifier.items()]}
        # Convertendo os dados atualizados em um formato que o MongoDB compreende
        data_to_set = {"$set": updatedData}

        result = collection.update_one(filter_query, data_to_set)

        return result.modified_count

    def delete(self, collection_name: str, dataIdentifier: dict):
        collection = self.connection[collection_name]

        filter_query = {"$and": [{field: value}
                                 for field, value in dataIdentifier.items()]}

        # é possível também usar o delete_many.
        result = collection.delete_one(filter_query)
        return result.deleted_count

    def closeConnection(self):
        if self._mongodb:
            # confirmar: Fechar usando client e não o db. Fazer MongoDatabase retornar o client e não o db direto.
            self._mongodb.close()
