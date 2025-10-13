# dao/estado_dispositivo_dao.py
from dominio.dispositivos.estado_dispositivo import EstadoDispositivo
from conn.conn_db import DBConnection
from dao.interfaces.i_estado_dispositivo_dao import IEstadoDispositivoDAO
from datetime import datetime

class EstadoDispositivoDAO(IEstadoDispositivoDAO):
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS estado_dispositivo (
                    id_estado INTEGER PRIMARY KEY AUTOINCREMENT,
                    estado_actual TEXT,
                    ultima_actualizacion TEXT
                )
            """)

    def agregar_estado(self, estado: EstadoDispositivo) -> int:
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT INTO estado_dispositivo (estado_actual, ultima_actualizacion) VALUES (?, ?)",
                (estado.estado_actual, estado.ultima_actualizacion.isoformat())
            )
            return cursor.lastrowid

    def obtener_estado(self, id_estado: int) -> EstadoDispositivo:
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT estado_actual, ultima_actualizacion FROM estado_dispositivo WHERE id_estado=?",
                (id_estado,)
            )
            fila = cursor.fetchone()
            if fila:
                e = EstadoDispositivo(fila[0])
                e._ultima_actualizacion = datetime.fromisoformat(fila[1])
                return e
            return None

    def actualizar_estado(self, id_estado: int, nuevo_estado: str):
        with DBConnection() as cursor:
            cursor.execute(
                "UPDATE estado_dispositivo SET estado_actual=?, ultima_actualizacion=? WHERE id_estado=?",
                (nuevo_estado, datetime.now().isoformat(), id_estado)
            )

    def eliminar_estado(self, id_estado: int):
        with DBConnection() as cursor:
            cursor.execute("DELETE FROM estado_dispositivo WHERE id_estado=?", (id_estado,))
