from dominio.usuarios.base import Usuario
from dominio.dispositivos.dispositivo import Dispositivo
from conn.conn_db import DBConnection


class UsuarioDispositivoDAO:
    def __init__(self):
        """Verifica que la tabla UsuariosDispositivos exista (ya existe en MySQL)."""
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT COUNT(*) FROM UsuariosDispositivos")
                print("Tabla UsuariosDispositivos verificada")
        except Exception as e:
            print(f"Error: {e}")
            raise

    def asignar_dispositivo(self, id_usuario: int, id_dispositivo: int):
        """Asigna un dispositivo a un usuario."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "INSERT IGNORE INTO UsuariosDispositivos (id_usuario, id_dispositivo) VALUES (%s, %s)",
                    (id_usuario, id_dispositivo)
                )
        except Exception as e:
            print(f"Error al asignar dispositivo: {e}")
            raise

    def quitar_dispositivo(self, id_usuario: int, id_dispositivo: int):
        """Quita un dispositivo de un usuario."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "DELETE FROM UsuariosDispositivos WHERE id_usuario=%s AND id_dispositivo=%s",
                    (id_usuario, id_dispositivo)
                )
        except Exception as e:
            print(f"Error al quitar dispositivo: {e}")
            raise

    def obtener_dispositivos_de_usuario(self, id_usuario: int):
        """Obtiene todos los dispositivos de un usuario."""
        try:
            with DBConnection() as cursor:
                cursor.execute("""
                    SELECT d.id_dispositivo, d.nombre, d.tipo_dispositivo
                    FROM Dispositivo d
                    JOIN UsuariosDispositivos ud ON d.id_dispositivo = ud.id_dispositivo
                    WHERE ud.id_usuario = %s
                """, (id_usuario,))
                filas = cursor.fetchall()
                return [
                    Dispositivo(id_dispositivo=f[0], nombre=f[1], tipo_dispositivo=f[2])
                    for f in filas
                ]
        except Exception as e:
            print(f"Error al obtener dispositivos de usuario: {e}")
            raise

    def obtener_usuarios_de_dispositivo(self, id_dispositivo: int):
        """Obtiene todos los usuarios de un dispositivo."""
        try:
            with DBConnection() as cursor:
                cursor.execute("""
                    SELECT u.id_usuario, u.usuario, u.email, u.contrasena, u.rol
                    FROM Usuario u
                    JOIN UsuariosDispositivos ud ON u.id_usuario = ud.id_usuario
                    WHERE ud.id_dispositivo = %s
                """, (id_dispositivo,))
                filas = cursor.fetchall()
                return [
                    Usuario(id_usuario=f[0], usuario=f[1], email=f[2], contraseña=f[3], rol=f[4])
                    for f in filas
                ]
        except Exception as e:
            print(f"Error al obtener usuarios de dispositivo: {e}")
            raise