from dao.interfaces.i_usuario_dao import IUsuarioDAO
from dominio.usuarios.base import Usuario
from dominio.usuarios.administrador import Administrador
from conn.conn_db import DBConnection

class UsuarioDAO(IUsuarioDAO):
    def __init__(self):
        with DBConnection() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Usuario (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    contraseña TEXT NOT NULL,
                    rol TEXT DEFAULT 'General'
                )
            """)

    def agregar_usuario(self, usuario: Usuario):
        with DBConnection() as cursor:
            cursor.execute("""
                INSERT INTO Usuario (usuario, email, contraseña, rol)
                VALUES (?, ?, ?, ?)
            """, (usuario.usuario, usuario.email, usuario._contraseña, usuario.rol))

    def obtener_usuario(self, nombre_usuario: str) -> Usuario:
        with DBConnection() as cursor:
            cursor.execute("""
                SELECT id_usuario, usuario, email, contraseña, rol
                FROM Usuario
                WHERE usuario = ?
            """, (nombre_usuario,))
            fila = cursor.fetchone()
            if fila:
                id_usuario, nombre, email, contraseña, rol = fila
                if rol.lower() == "admin":
                    return Administrador(id_usuario=id_usuario, usuario=nombre, email=email, contraseña=contraseña)
                else:
                    return Usuario(id_usuario=id_usuario, usuario=nombre, email=email, contraseña=contraseña, rol=rol)
            return None

    def actualizar_usuario(self, usuario: Usuario):
        with DBConnection() as cursor:
            cursor.execute("""
                UPDATE Usuario
                SET email = ?, contraseña = ?, rol = ?
                WHERE usuario = ?
            """, (usuario.email, usuario._contraseña, usuario.rol, usuario.usuario))

    def eliminar_usuario(self, usuario: Usuario):
        with DBConnection() as cursor:
            cursor.execute("""
                DELETE FROM Usuario
                WHERE usuario = ?
            """, (usuario.usuario,))
