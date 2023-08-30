class PersonRepository:
    def __init__(self, database_strategy) -> None:
        self._strategy = database_strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, database_strategy):
        self._strategy = database_strategy

    def find_person_by_id(self):
        pass

    def insert_person(self):
        pass

    def update_person(self):
        pass

    def delete_person(self):
        pass
