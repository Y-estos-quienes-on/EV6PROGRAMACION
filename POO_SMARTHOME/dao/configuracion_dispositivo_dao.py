from dominio.dispositivos.configuracion_dispositivo import ConfiguracionDispositivo
from conn.conn_db import DBConnection
from datetime import datetime


class ConfiguracionDispositivoDAO:
    def __init__(self):
        """Verifica que la tabla Configuracion_Dispositivo exista (ya existe en MySQL)."""
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Configuracion_Dispositivo")
                print("Tabla Configuracion_Dispositivo verificada")
        except Exception as e:
            print(f"Error: {e}")
            raise

    def agregar_configuracion(self, config: ConfiguracionDispositivo) -> int:
        """Inserta una nueva configuración."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "INSERT INTO Configuracion_Dispositivo (estado, configuracion, time_stamp) VALUES (%s, %s, %s)",
                    (config.estado, config.configuracion, config.time_stamp)
                )
                return cursor.lastrowid
        except Exception as e:
            print(f"Error al agregar configuración: {e}")
            raise

    def obtener_configuracion(self, id_config: int):
        """Obtiene una configuración por ID."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "SELECT estado, configuracion, time_stamp FROM Configuracion_Dispositivo WHERE id_configuracion=%s",
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
        except Exception as e:
            print(f"Error al obtener configuración: {e}")
            raise

    def actualizar_configuracion(self, id_config: int, config: ConfiguracionDispositivo):
        """Actualiza una configuración."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "UPDATE Configuracion_Dispositivo SET estado=%s, configuracion=%s, time_stamp=%s WHERE id_configuracion=%s",
                    (config.estado, config.configuracion, datetime.now(), id_config)
                )
        except Exception as e:
            print(f"Error al actualizar configuración: {e}")
            raise

    def eliminar_configuracion(self, id_config: int):
        """Elimina una configuración."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "DELETE FROM Configuracion_Dispositivo WHERE id_configuracion=%s",
                    (id_config,)
                )
        except Exception as e:
            print(f"Error al eliminar configuración: {e}")
            raise