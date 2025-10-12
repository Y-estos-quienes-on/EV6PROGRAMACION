from dominio.dispositivos.configuracion_dispositivo import ConfiguracionDispositivo
from conn.conn_db import DBConnection
from dao.interfaces.i_configuracion_dispositivo_dao import IConfiguracionDispositivoDAO
from datetime import datetime

class ConfiguracionDispositivoDAO(IConfiguracionDispositivoDAO):
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS configuracion_dispositivo (
                    id_configuracion INTEGER PRIMARY KEY AUTOINCREMENT,
                    configuracion TEXT,
                    time_stamp TEXT
                )
            """)

    def agregar_configuracion(self, config: ConfiguracionDispositivo) -> int:
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT INTO configuracion_dispositivo (configuracion, time_stamp) VALUES (?, ?)",
                (config.configuracion, config.time_stamp.isoformat())
            )
            return cursor.lastrowid

    def obtener_configuracion(self, id_config: int) -> ConfiguracionDispositivo:
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT configuracion, time_stamp FROM configuracion_dispositivo WHERE id_configuracion=?",
                (id_config,)
            )
            fila = cursor.fetchone()
            if fila:
                c = ConfiguracionDispositivo(fila[0])
                c._time_stamp = datetime.fromisoformat(fila[1])
                return c
            return None

    def actualizar_configuracion(self, id_config: int, nueva_config: str):
        with DBConnection() as cursor:
            cursor.execute(
                "UPDATE configuracion_dispositivo SET configuracion=?, time_stamp=? WHERE id_configuracion=?",
                (nueva_config, datetime.now().isoformat(), id_config)
            )

    def eliminar_configuracion(self, id_config: int):
        with DBConnection() as cursor:
            cursor.execute("DELETE FROM configuracion_dispositivo WHERE id_configuracion=?", (id_config,))