from dominio.dispositivos.estado_dispositivo import EstadoDispositivo
from conn.conn_db import DBConnection
from datetime import datetime

class EstadoDispositivoDAO:
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estado_Dispositivo (
                    id_estado INTEGER PRIMARY KEY AUTOINCREMENT,
                    estado_actual TEXT,
                    ultima_actualizacion DATETIME
                )
            """)

    def agregar_estado(self, estado: EstadoDispositivo) -> int:
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT INTO Estado_Dispositivo (estado_actual, ultima_actualizacion) VALUES (?, ?)",
                (estado.estado_actual, estado.ultima_actualizacion)
            )
            return cursor.lastrowid

    def obtener_estado(self, id_estado: int):
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT estado_actual, ultima_actualizacion FROM Estado_Dispositivo WHERE id_estado=?",
                (id_estado,)
            )
            fila = cursor.fetchone()
            if fila:
                return {
                    "estado_actual": fila[0],
                    "ultima_actualizacion": fila[1]
                }
            return None

    def actualizar_estado(self, id_estado: int, estado: EstadoDispositivo):
        with DBConnection() as cursor:
            cursor.execute(
                "UPDATE Estado_Dispositivo SET estado_actual=?, ultima_actualizacion=? WHERE id_estado=?",
                (estado.estado_actual, datetime.now(), id_estado)
            )

    def eliminar_estado(self, id_estado: int):
        with DBConnection() as cursor:
            cursor.execute("DELETE FROM Estado_Dispositivo WHERE id_estado=?", (id_estado,))
