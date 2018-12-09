import sqlite3


class SQLConnector(object):
    def _connect(self):
        self._connection = sqlite3.connect('app/rafflemaker.db')
        self._connection.row_factory = sqlite3.Row
        self._cursor = self._connection.cursor()

    def _query(self, query, *args):
        self._connect()
        return self._cursor.execute(query, args[0])

    def query_insert(self, query, *args):
        self._query(query, args[0])
        self._commit()
        self._close()

    def query_update(self, query, *args):
        self._query(query, args[0])
        self._commit()
        self._close()

    def query_delete(self, query, *args):
        self._query(query, args[0])
        self._commit()
        self._close()

    def _get_one(self):
        result = self._cursor.fetchone()
        self._close()

        return result

    def query_get_one(self, query, *args):
        self._query(query, args[0])
        result = self._get_one()

        return result

    def _get_all(self):
        result = self._cursor.fetchall()
        self._close()

        return result

    def query_get_all(self, query, *args):
        self._query(query, args[0])
        result = self._get_all()

        return result

    def _commit(self):
        self._connection.commit()

    def _close(self):
        self._connection.close()
