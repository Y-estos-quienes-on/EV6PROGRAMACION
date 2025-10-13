from dominio.dispositivos.configuracion_dispositivo import ConfiguracionDispositivo
from conn.conn_db import DBConnection
from datetime import datetime

class ConfiguracionDispositivoDAO:
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Configuracion_Dispositivo (
                    id_configuracion INTEGER PRIMARY KEY AUTOINCREMENT,
                    estado INTEGER,
                    configuracion TEXT,
                    time_stamp TEXT
                )
            """)

    def agregar_configuracion(self, config: ConfiguracionDispositivo) -> int:
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT INTO Configuracion_Dispositivo (estado, configuracion, time_stamp) VALUES (?, ?, ?)",
                (1 if config.configuracion else 0, config.configuracion, config.time_stamp)
            )
            return cursor.lastrowid

    def obtener_configuracion(self, id_config: int):
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT estado, configuracion, time_stamp FROM Configuracion_Dispositivo WHERE id_configuracion=?",
                (id_config,)
            )
            fila = cursor.fetchone()
            if fila:
                return {
                    "estado": bool(fila[0]),
                    "configuracion": fila[1],
                    "time_stamp": fila[2]
                }
            return None

    def actualizar_configuracion(self, id_config: int, config: ConfiguracionDispositivo):
        with DBConnection() as cursor:
            cursor.execute(
                "UPDATE Configuracion_Dispositivo SET estado=?, configuracion=?, time_stamp=? WHERE id_configuracion=?",
                (1 if config.configuracion else 0, config.configuracion, datetime.now(), id_config)
            )

    def eliminar_configuracion(self, id_config: int):
        with DBConnection() as cursor:
            cursor.execute(
                "DELETE FROM Configuracion_Dispositivo WHERE id_configuracion=?",
                (id_config,)
            )