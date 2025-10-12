from dao.interfaces.i_usuario_dao import IUsuarioDAO
from dominio.usuarios.base import Usuario
from dominio.usuarios.administrador import Administrador
from conn.conn_db import DBConnection

class UsuarioDAO(IUsuarioDAO):
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    usuario TEXT PRIMARY KEY,
                    email TEXT,
                    contraseña TEXT,
                    rol TEXT
                )
            """)

    def agregar_usuario(self, usuario: Usuario):
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (usuario, email, contraseña, rol) VALUES (?, ?, ?, ?)",
                (usuario.usuario, usuario.email, usuario._contraseña, usuario.rol)
            )

    def obtener_usuario(self, usuario_nombre: str) -> Usuario:
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT usuario, email, contraseña, rol FROM usuarios WHERE usuario=?",
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

    def actualizar_usuario(self, usuario: Usuario):
        with DBConnection() as cursor:
            cursor.execute(
                "UPDATE usuarios SET email=?, contraseña=?, rol=? WHERE usuario=?",
                (usuario.email, usuario._contraseña, usuario.rol, usuario.usuario)
            )

    def eliminar_usuario(self, usuario: Usuario):
        with DBConnection() as cursor:
            cursor.execute(
                "DELETE FROM usuarios WHERE usuario=?",
                (usuario.usuario,)
            )
