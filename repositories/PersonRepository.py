from Repository import Repository


class PersonRepository(Repository):
    def __init__(self, database_strategy) -> None:
        self._database_strategy = database_strategy

    @property
    def database_strategy(self):
        return self._database_strategy

    @database_strategy.setter
    def strategy(self, database_strategy):
        self._database_strategy = database_strategy

    def findAll(self, *args):
        pass

    def findOneByData(self, *args):
        pass

    def insert(self, *args):
        pass

    def update(self, *args):
        pass

    def delete(self, *args):
        pass
