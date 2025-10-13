from dominio.usuarios.base import Usuario
from dominio.dispositivos.dispositivo import Dispositivo
from conn.conn_db import DBConnection

class UsuarioDispositivoDAO:
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS UsuariosDispositivos (
                    id_usuario INTEGER NOT NULL,
                    id_dispositivo INTEGER NOT NULL,
                    PRIMARY KEY (id_usuario, id_dispositivo),
                    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
                    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo)
                )
            """)

    def asignar_dispositivo(self, id_usuario: int, id_dispositivo: int):
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT OR IGNORE INTO UsuariosDispositivos (id_usuario, id_dispositivo) VALUES (?, ?)",
                (id_usuario, id_dispositivo)
            )

    def quitar_dispositivo(self, id_usuario: int, id_dispositivo: int):
        with DBConnection() as cursor:
            cursor.execute(
                "DELETE FROM UsuariosDispositivos WHERE id_usuario=? AND id_dispositivo=?",
                (id_usuario, id_dispositivo)
            )

    def obtener_dispositivos_de_usuario(self, id_usuario: int):
        with DBConnection() as cursor:
            cursor.execute("""
                SELECT d.id_dispositivo, d.nombre, d.tipo_dispositivo
                FROM Dispositivo d
                JOIN UsuariosDispositivos ud ON d.id_dispositivo = ud.id_dispositivo
                WHERE ud.id_usuario = ?
            """, (id_usuario,))
            filas = cursor.fetchall()
            return [
                Dispositivo(nombre=f[1], tipo_dispositivo=f[2])
                for f in filas
            ]

    def obtener_usuarios_de_dispositivo(self, id_dispositivo: int):
        with DBConnection() as cursor:
            cursor.execute("""
                SELECT u.id_usuario, u.usuario, u.email, u.contraseña, u.rol
                FROM Usuario u
                JOIN UsuariosDispositivos ud ON u.id_usuario = ud.id_usuario
                WHERE ud.id_dispositivo = ?
            """, (id_dispositivo,))
            filas = cursor.fetchall()
            return [
                Usuario(usuario=f[1], email=f[2], contraseña=f[3], rol=f[4])
                for f in filas
            ]
