from dominio.dispositivos.dispositivo import Dispositivo
from conn.conn_db import DBConnection

class DispositivoDAO:
    def __init__(self):
        """Verifica que la tabla Dispositivo exista."""
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Dispositivo")
                print("Tabla Dispositivo verificada")
        except Exception as e:
            print(f"Error: {e}")
            raise

    def agregar_dispositivo(self, dispositivo: Dispositivo, id_estado: int, id_config: int):
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "INSERT INTO Dispositivo (nombre, tipo_dispositivo, id_estado, id_configuracion) VALUES (%s, %s, %s, %s)",
                    (dispositivo.nombre, dispositivo.tipo_dispositivo, id_estado, id_config)
                )
                return cursor.lastrowid
        except Exception as e:
            print(f"Error al agregar dispositivo: {e}")
            raise

    def obtener_dispositivo(self, id_dispositivo):
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "SELECT * FROM Dispositivo WHERE id_dispositivo=%s",
                    (id_dispositivo,)
                )
                return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener dispositivo: {e}")
            raise

    def actualizar_dispositivo(self, id_dispositivo, nombre=None, tipo=None):
        try:
            with DBConnection() as cursor:
                if nombre:
                    cursor.execute(
                        "UPDATE Dispositivo SET nombre=%s WHERE id_dispositivo=%s",
                        (nombre, id_dispositivo)
                    )
                if tipo:
                    cursor.execute(
                        "UPDATE Dispositivo SET tipo_dispositivo=%s WHERE id_dispositivo=%s",
                        (tipo, id_dispositivo)
                    )
        except Exception as e:
            print(f"Error al actualizar dispositivo: {e}")
            raise

    def eliminar_dispositivo(self, id_dispositivo):
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "DELETE FROM Dispositivo WHERE id_dispositivo=%s",
                    (id_dispositivo,)
                )
        except Exception as e:
            print(f"Error al eliminar dispositivo: {e}")
            raise

    def obtener_todos_dispositivos(self):
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT * FROM Dispositivo")
                return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar dispositivos: {e}")
            raise