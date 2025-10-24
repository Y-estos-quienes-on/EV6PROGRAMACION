from dominio.dispositivos.estado_dispositivo import EstadoDispositivo
from conn.conn_db import DBConnection
from datetime import datetime


class EstadoDispositivoDAO:
    def __init__(self):
        """Verifica que la tabla Estado_Dispositivo exista (ya existe en MySQL)."""
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Estado_Dispositivo")
                print("Tabla Estado_Dispositivo verificada")
        except Exception as e:
            print(f"Error: {e}")
            raise

    def agregar_estado(self, estado: EstadoDispositivo) -> int:
        """Inserta un nuevo estado de dispositivo."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "INSERT INTO Estado_Dispositivo (estado_actual, ultima_actualizacion) VALUES (%s, %s)",
                    (estado.estado_actual, estado.ultima_actualizacion)
                )
                return cursor.lastrowid
        except Exception as e:
            print(f"Error al agregar estado: {e}")
            raise

    def obtener_estado(self, id_estado: int):
        """Obtiene un estado por ID."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "SELECT estado_actual, ultima_actualizacion FROM Estado_Dispositivo WHERE id_estado=%s",
                    (id_estado,)
                )
                fila = cursor.fetchone()
                if fila:
                    return {
                        "estado_actual": fila[0],
                        "ultima_actualizacion": fila[1]
                    }
                return None
        except Exception as e:
            print(f"Error al obtener estado: {e}")
            raise

    def actualizar_estado(self, id_estado: int, estado: EstadoDispositivo):
        """Actualiza el estado de un dispositivo."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "UPDATE Estado_Dispositivo SET estado_actual=%s, ultima_actualizacion=%s WHERE id_estado=%s",
                    (estado.estado_actual, datetime.now(), id_estado)
                )
        except Exception as e:
            print(f"Error al actualizar estado: {e}")
            raise

    def eliminar_estado(self, id_estado: int):
        """Elimina un estado."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "DELETE FROM Estado_Dispositivo WHERE id_estado=%s",
                    (id_estado,)
                )
        except Exception as e:
            print(f"Error al eliminar estado: {e}")
            raise