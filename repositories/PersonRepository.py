from Repository import Repository


class PersonRepository(Repository):
    def __init__(self, database_strategy) -> None:
        self._strategy = database_strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, database_strategy):
        self._strategy = database_strategy

    def findAll(self, *args):
        pass

    def find_by_id(self, *args):
        pass

    def insert(self, *args):
        pass

    def update(self, *args):
        pass

    def delete(self, *args):
        pass
