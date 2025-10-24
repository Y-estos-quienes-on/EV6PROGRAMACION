import mysql.connector
from mysql.connector import Error

class DBConnection:
    def __init__(self, host="localhost", user="root", password="root", database="SmartHome"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                autocommit=False
            )
            self.cursor = self.conn.cursor(buffered=True)
            return self.cursor
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn and self.conn.is_connected():
                if exc_type is None:
                    self.conn.commit()
                else:
                    self.conn.rollback()
                self.conn.close()
        except Error as e:
            print(f"Error al cerrar conexión: {e}")