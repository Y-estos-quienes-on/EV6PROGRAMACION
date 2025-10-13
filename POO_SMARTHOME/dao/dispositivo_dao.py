from dominio.dispositivos.dispositivo import Dispositivo
from conn.conn_db import DBConnection

class DispositivoDAO:
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Dispositivo (
                    id_dispositivo INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    tipo_dispositivo TEXT,
                    id_estado INTEGER,
                    id_configuracion INTEGER
                )
            """)

    def agregar_dispositivo(self, dispositivo: Dispositivo, id_estado: int, id_config: int):
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT INTO Dispositivo (nombre, tipo_dispositivo, id_estado, id_configuracion) VALUES (?, ?, ?, ?)",
                (dispositivo.nombre, dispositivo.tipo_dispositivo, id_estado, id_config)
            )
            return cursor.lastrowid

    def obtener_dispositivo(self, id_dispositivo):
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT * FROM Dispositivo WHERE id_dispositivo=?",
                (id_dispositivo,)
            )
            return cursor.fetchone()
        
    def actualizar_dispositivo(self, id_dispositivo, nombre=None, tipo=None):
        with DBConnection() as cursor:
            if nombre:
                cursor.execute("UPDATE Dispositivo SET nombre=? WHERE id_dispositivo=?", (nombre, id_dispositivo))
            if tipo:
                cursor.execute("UPDATE Dispositivo SET tipo_dispositivo=? WHERE id_dispositivo=?", (tipo, id_dispositivo))

    def eliminar_dispositivo(self, id_dispositivo):
        with DBConnection() as cursor:
            cursor.execute("DELETE FROM Dispositivo WHERE id_dispositivo=?", (id_dispositivo,))

    def obtener_todos_dispositivos(self):
        with DBConnection() as cursor:
            cursor.execute("SELECT * FROM Dispositivo")
            return cursor.fetchall()
