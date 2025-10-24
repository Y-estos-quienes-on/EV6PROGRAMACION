from conn.conn_db import DBConnection
from datetime import datetime


class ConsentimientoPrivacidadDAO:
    def __init__(self):
        """Verifica que la tabla ConsentimientoPrivacidad exista (ya existe en MySQL)."""
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT COUNT(*) FROM ConsentimientoPrivacidad")
                print("Tabla ConsentimientoPrivacidad verificada")
        except Exception as e:
            print(f"Error: {e}")
            raise

    def registrar_consentimiento(self, id_usuario: int, aceptado: bool):
        """Registra un nuevo consentimiento."""
        try:
            fecha = datetime.now()
            with DBConnection() as cursor:
                cursor.execute(
                    "INSERT INTO ConsentimientoPrivacidad (acepta_politicas, fecha, id_usuario) VALUES (%s, %s, %s)",
                    (int(aceptado), fecha, id_usuario)
                )
        except Exception as e:
            print(f"Error al registrar consentimiento: {e}")
            raise

    def obtener_consentimiento(self, id_usuario: int):
        """Obtiene el último consentimiento de un usuario."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "SELECT acepta_politicas, fecha FROM ConsentimientoPrivacidad WHERE id_usuario=%s ORDER BY fecha DESC LIMIT 1",
                    (id_usuario,)
                )
                fila = cursor.fetchone()
                if fila:
                    return {"acepta_politicas": bool(fila[0]), "fecha": fila[1]}
                return {"acepta_politicas": False, "fecha": None}
        except Exception as e:
            print(f"Error al obtener consentimiento: {e}")
            raise

    def actualizar_consentimiento(self, id_usuario: int, aceptado: bool):
        """Actualiza el consentimiento de un usuario."""
        try:
            fecha = datetime.now()
            with DBConnection() as cursor:
                cursor.execute(
                    "UPDATE ConsentimientoPrivacidad SET acepta_politicas=%s, fecha=%s WHERE id_usuario=%s",
                    (int(aceptado), fecha, id_usuario)
                )
        except Exception as e:
            print(f"Error al actualizar consentimiento: {e}")
            raise