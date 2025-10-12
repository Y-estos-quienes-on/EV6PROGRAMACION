from dao.interfaces.i_usuario_dao import IUsuarioDAO
from dominio.usuarios.base import Usuario
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

    def agregarUsuario(self, usuario: Usuario):
        with DBConnection() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (usuario, email, contraseña, rol) VALUES (?, ?, ?, ?)",
                (usuario.usuario, usuario.email, usuario._Usuario__contraseña, usuario.rol)
            )

    def obtenerUsuario(self, usuario_nombre: str) -> Usuario:
        with DBConnection() as cursor:
            cursor.execute(
                "SELECT usuario, email, contraseña, rol FROM usuarios WHERE usuario=?",
                (usuario_nombre,)
            )
            fila = cursor.fetchone()
            if fila:
                u = Usuario(fila[0], fila[1], "temp1234", fila[3])      
                u._Usuario__contraseña = fila[2]
                return u
            return None

    def actualizarUsuario(self, usuario: Usuario):
        with DBConnection() as cursor:
            cursor.execute(
                "UPDATE usuarios SET email=?, contraseña=?, rol=? WHERE usuario=?",
                (usuario.email, usuario._Usuario__contraseña, usuario.rol, usuario.usuario)
            )

    def eliminarUsuario(self, usuario: Usuario):
        with DBConnection() as cursor:
            cursor.execute("DELETE FROM usuarios WHERE usuario=?", (usuario.usuario,))
