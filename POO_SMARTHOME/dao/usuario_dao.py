from dao.interfaces.i_usuario_dao import IUsuarioDAO
from dominio.usuarios.base import Usuario
from dominio.usuarios.administrador import Administrador
from conn.conn_db import DBConnection


class UsuarioDAO(IUsuarioDAO):
    def __init__(self):
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Usuario")
                print("Tabla Usuario verificada")
        except Exception as e:
            print(f"Error: {e}")
            raise

    def agregar_usuario(self, usuario: Usuario):
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "INSERT INTO Usuario (usuario, email, contrasena, rol) VALUES (%s, %s, %s, %s)",
                    (usuario.usuario, usuario.email, usuario._contraseña, usuario.rol)
                )
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            raise

    def obtener_usuario(self, nombre_usuario: str) -> Usuario:
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "SELECT id_usuario, usuario, email, contrasena, rol FROM Usuario WHERE usuario=%s",
                    (nombre_usuario,)
                )
                fila = cursor.fetchone()
                if fila:
                    id_usuario, nombre, email, contraseña, rol = fila
                    if rol.lower() == "admin":
                        return Administrador(id_usuario=id_usuario, usuario=nombre, email=email, contraseña=contraseña)
                    else:
                        return Usuario(id_usuario=id_usuario, usuario=nombre, email=email, contraseña=contraseña, rol=rol)
                return None
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            raise

    def actualizar_usuario(self, usuario: Usuario):
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
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "DELETE FROM Usuario WHERE usuario=%s",
                    (usuario.usuario,)
                )
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            raise