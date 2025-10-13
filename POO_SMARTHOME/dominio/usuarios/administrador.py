
from dominio.usuarios.base import Usuario


class Administrador(Usuario):
    def __init__(self, usuario, email, contraseña):
        super().__init__(usuario, email, contraseña, rol="admin")

    #Cambiar Rol
    def modificar_rol(self, otro_usuario, nuevo_rol):
        """Permite al admin cambiar el rol de otro usuario."""
        if nuevo_rol not in Usuario.ROLES_VALIDOS:
            raise ValueError("Rol inválido")
        otro_usuario._rol = nuevo_rol
