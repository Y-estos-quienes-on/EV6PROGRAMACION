import sqlite3
import mysql.connector

DB_TYPE = "sqlite"
MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "SmartHome"
}
SQLITE_NAME = "app.db"

class DBConnection:
    def __enter__(self):
        if DB_TYPE == "mysql":
            self.conn = mysql.connector.connect(**MYSQL_CONFIG)
            self.cursor = self.conn.cursor(dictionary=True)
        else:
            self.conn = sqlite3.connect(SQLITE_NAME)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        self.conn.close()
