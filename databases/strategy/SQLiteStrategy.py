from adapters.RelationalAdapter import RelationalAdapter
from sqlite3 import Row
from utils import getWhereClauseConditions


class SQLiteStrategy(RelationalAdapter):
    def __init__(self, sqlitedb_instance):
        self._sqlitedb = sqlitedb_instance
        # allowing search by column name property in fetchall and fetchone results.
        self._sqlitedb = Row
        self._placeholder = "?"

    @property
    def connection(self):
        return self._sqlitedb

    @property
    def cursor(self):
        return self.connection.cursor()

    @property
    def placeholder_sqlite(self):
        return self._placeholder

    def create_table(self, table_name: str, table_schema: dict):
        schema_columns = ','.join(
            [f"{col_name} {col_type}" for col_name, col_type in table_schema.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ( {schema_columns} )"
        cursor = self.cursor
        cursor.execute(query)
        self.connection.commit()
        print(f"A tabela {table_name} foi criada com sucesso!")
        cursor.close()

    def findAll(self, table: str, fields: str = "*"):
        query = f"SELECT {fields} FROM {table}"
        cursor = self.cursor
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def findOneByData(self, table: str, dataToSearch: dict, fields: str = "*"):
        clause_conditions, clause_values = getWhereClauseConditions(
            dataToSearch, self.placeholder_sqlite)
        query = f"SELECT {fields} FROM {table} WHERE {clause_conditions}"
        cursor = self.cursor
        cursor.execute(query, clause_values)
        result = cursor.fetchone()
        cursor.close()
        return result

    def insert(self, table: str, dataToInsert: dict):
        columns = ",".join(dataToInsert.keys())
        placeholders = ",".join(
            [f"{self.placeholder_sqlite}"] * len(dataToInsert.keys()))
        values = tuple(dataToInsert.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor = self.cursor
        cursor.execute(query, values)
        self.connection.commit()
        last_id = cursor.lastrowid
        cursor.close()
        return last_id

    def update(self, table: str, dataIdentifier: dict, updatedData: dict):
        columns_to_update = ",".join(
            [f"{column}={self.placeholder_sqlite}" for column in updatedData.keys()])
        clause_conditions, clause_values = getWhereClauseConditions(
            dataIdentifier, self.placeholder_sqlite)
        values_to_update = tuple(updatedData.values()) + clause_values
        query = f"UPDATE {table} SET {columns_to_update} WHERE {clause_conditions}"
        cursor = self.cursor
        cursor.execute(query, values_to_update)
        self.connection.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        return rows_affected

    def delete(self, table: str, dataIdentifier: dict):
        clause_conditions, clause_values = getWhereClauseConditions(
            dataIdentifier, self.placeholder_sqlite)
        query = f"DELETE FROM {table} WHERE {clause_conditions}"
        cursor = self.cursor
        cursor.execute(query, clause_values)
        self.connection.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        return rows_affected

    def close_connection(self):
        if self.connection:
            self._sqlitedb.close()
            print("Conexão com o Sqlite encerrada com sucesso!")
