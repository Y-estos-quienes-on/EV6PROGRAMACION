from conn.conn_db import DBConnection
from datetime import datetime

class ConsentimientoPrivacidadDAO:
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ConsentimientoPrivacidad (
                    id_consentimiento INTEGER PRIMARY KEY AUTOINCREMENT,
                    acepta_politicas INTEGER,
                    fecha TEXT,
                    id_usuario INTEGER,
                    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
                )
            """)

    def registrar_consentimiento(self, id_usuario: int, aceptado: bool):
        fecha = datetime.now().isoformat()
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT INTO ConsentimientoPrivacidad (acepta_politicas, fecha, id_usuario) VALUES (?, ?, ?)",
                (int(aceptado), fecha, id_usuario)
            )

    def obtener_consentimiento(self, id_usuario: int):
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT acepta_politicas, fecha FROM ConsentimientoPrivacidad WHERE id_usuario=? ORDER BY fecha DESC LIMIT 1",
                (id_usuario,)
            )
            fila = cursor.fetchone()
            if fila:
                return {"acepta_politicas": bool(fila[0]), "fecha": fila[1]}
            return {"acepta_politicas": False, "fecha": None}

    def actualizar_consentimiento(self, id_usuario: int, aceptado: bool):
        fecha = datetime.now().isoformat()
        with DBConnection() as cursor:
            cursor.execute(
                "UPDATE ConsentimientoPrivacidad SET acepta_politicas=?, fecha=? WHERE id_usuario=?",
                (int(aceptado), fecha, id_usuario)
            )
