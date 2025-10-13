from dao.interfaces.i_usuario_dao import IUsuarioDAO
from dominio.usuarios.base import Usuario
from dominio.usuarios.administrador import Administrador
from conn.conn_db import DBConnection


class UsuarioDAO(IUsuarioDAO):
    def __init__(self):
        """
        No crea tabla porque ya existe en la BD.
        Solo verifica la conexión.
        """
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Usuario")
                print("✅ Tabla Usuario verificada")
        except Exception as e:
            print(f"❌ Error: {e}")
            raise

    def agregar_usuario(self, usuario: Usuario):
        """Inserta un nuevo usuario en la BD."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "INSERT INTO Usuario (usuario, email, contrasena, rol) VALUES (%s, %s, %s, %s)",
                    (usuario.usuario, usuario.email, usuario._contraseña, usuario.rol)
                )
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            raise

    def obtener_usuario(self, usuario_nombre: str) -> Usuario:
        """Obtiene un usuario por nombre."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "SELECT usuario, email, contrasena, rol FROM Usuario WHERE usuario=%s",
                    (usuario_nombre,)
                )
                fila = cursor.fetchone()
                if fila:
                    rol = fila[3].lower()
                    if rol == "admin":
                        return Administrador(fila[0], fila[1], fila[2])
                    else:
                        return Usuario(fila[0], fila[1], fila[2], rol)
                return None
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            raise

    def actualizar_usuario(self, usuario: Usuario):
        """Actualiza un usuario existente."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "UPDATE Usuario SET email=%s, contrasena=%s, rol=%s WHERE usuario=%s",
                    (usuario.email, usuario._contraseña, usuario.rol, usuario.usuario)
                )
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            raise

    def eliminar_usuario(self, usuario: Usuario):
        """Elimina un usuario de la BD."""
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "DELETE FROM Usuario WHERE usuario=%s",
                    (usuario.usuario,)
                )
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            raise