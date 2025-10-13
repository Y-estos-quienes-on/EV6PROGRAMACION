from conn.conn_db import DBConnection
from dao.interfaces.i_consentimiento_privacidad import IConsentimientoPrivacidadDAO

class ConsentimientoPrivacidadDAO(IConsentimientoPrivacidadDAO):
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS consentimiento_privacidad (
                    usuario TEXT PRIMARY KEY,
                    aceptado INTEGER
                )
            """)

    # Método requerido por la interfaz
    def registrar_consentimiento(self, usuario: str, aceptado: bool):
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT OR REPLACE INTO consentimiento_privacidad (usuario, aceptado) VALUES (?, ?)",
                (usuario, int(aceptado))
            )

    # Método requerido por la interfaz
    def verificar_consentimiento(self, usuario: str) -> bool:
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT aceptado FROM consentimiento_privacidad WHERE usuario=?",
                (usuario,)
            )
            fila = cursor.fetchone()
            return bool(fila[0]) if fila else False

    # Opcional: métodos adicionales para tu servicio
    def actualizar_consentimiento(self, usuario: str, aceptado: bool):
        with DBConnection() as cursor:
            cursor.execute(
                "UPDATE consentimiento_privacidad SET aceptado=? WHERE usuario=?",
                (int(aceptado), usuario)
            )

    def obtener_consentimiento(self, usuario: str) -> bool:
        return self.verificar_consentimiento(usuario)
