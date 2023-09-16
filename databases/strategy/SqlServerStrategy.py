from adapters.RelationalAdapter import RelationalAdapter
from utils import getWhereClauseConditions


class SQLServerStrategy(RelationalAdapter):
    def __init__(self, sqlserver_instance):
        self._sqlserver = sqlserver_instance
        self._placeholder = "?"

    @property
    def connection(self):
        return self._sqlserver

    @property
    def cursor(self):
        return self.connection.cursor()

    @property
    def placeholder_sqlserver(self):
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
            dataToSearch, self.placeholder_sqlserver)
        query = f"SELECT {fields} FROM {table} WHERE {clause_conditions}"
        cursor = self.cursor
        cursor.execute(query, clause_values)
        result = cursor.fetchone()
        cursor.close()
        return result

    def insert(self, table: str, dataToInsert: dict):
        columns = ",".join(dataToInsert.keys())
        placeholders = ",".join(
            [f"{self.placeholder_sqlserver}"] * len(dataToInsert.keys()))
        values = tuple(dataToInsert.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor = self.cursor
        cursor.execute(query, values)
        self.connection.commit()
        # get the last ID inserted in sql server
        cursor.execute("SELECT SCOPE_IDENTITY()")
        last_id = cursor.fetchone()[0]
        cursor.close()
        return last_id

    def update(self, table: str, dataIdentifier: dict, updatedData: dict):
        columns_to_update = ",".join(
            [f"{column}={self.placeholder_sqlserver}" for column in updatedData.keys()])
        clause_conditions, clause_values = getWhereClauseConditions(
            dataIdentifier, self.placeholder_sqlserver)
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
            dataIdentifier, self.placeholder_sqlserver)
        query = f"DELETE FROM {table} WHERE {clause_conditions}"
        cursor = self.cursor
        cursor.execute(query, clause_values)
        self.connection.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        return rows_affected

    def close_connection(self):
        if self.connection:
            self._sqlserver.close()
            print("Conexão com o SQL Server encerrada com sucesso!")
