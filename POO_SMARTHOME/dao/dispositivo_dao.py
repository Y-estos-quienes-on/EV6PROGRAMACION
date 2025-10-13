from dominio.dispositivos.dispositivo import Dispositivo
from dao.estado_dispositivo_dao import EstadoDispositivoDAO
from dao.configuracion_dispositivo_dao import ConfiguracionDispositivoDAO
from dao.interfaces.i_dispositivo_dao import IDispositivoDAO
from conn.conn_db import DBConnection

class DispositivoDAO(IDispositivoDAO):
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS dispositivo (
                    id_dispositivo INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    tipo_dispositivo TEXT,
                    id_estado INTEGER,
                    id_configuracion INTEGER,
                    FOREIGN KEY (id_estado) REFERENCES estado_dispositivo(id_estado),
                    FOREIGN KEY (id_configuracion) REFERENCES configuracion_dispositivo(id_configuracion)
                )
            """)

    def agregar_dispositivo(self, dispositivo: Dispositivo, id_estado: int, id_config: int) -> int:
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT INTO dispositivo (nombre, tipo_dispositivo, id_estado, id_configuracion) VALUES (?, ?, ?, ?)",
                (dispositivo.nombre, dispositivo.tipo_dispositivo, id_estado, id_config)
            )
            return cursor.lastrowid

    def obtener_dispositivo(self, id_dispositivo: int):
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT nombre, tipo_dispositivo, id_estado, id_configuracion FROM dispositivo WHERE id_dispositivo=?",
                (id_dispositivo,)
            )
            return cursor.fetchone()

    def actualizar_dispositivo(self, id_dispositivo: int, nombre: str = None, tipo: str = None):
        with DBConnection() as cursor:
            if nombre:
                cursor.execute("UPDATE dispositivo SET nombre=? WHERE id_dispositivo=?", (nombre, id_dispositivo))
            if tipo:
                cursor.execute("UPDATE dispositivo SET tipo_dispositivo=? WHERE id_dispositivo=?", (tipo, id_dispositivo))

    def eliminar_dispositivo(self, id_dispositivo: int):
        with DBConnection() as cursor:
            cursor.execute("DELETE FROM dispositivo WHERE id_dispositivo=?", (id_dispositivo,))

    def obtener_todos_dispositivos(self):
        with DBConnection() as cursor:
            cursor.execute("SELECT id_dispositivo, nombre, tipo_dispositivo, id_estado, id_configuracion FROM dispositivo")
            return cursor.fetchall()