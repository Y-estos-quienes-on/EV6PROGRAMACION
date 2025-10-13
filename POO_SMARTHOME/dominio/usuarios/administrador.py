from dominio.usuarios.base import Usuario

class Administrador(Usuario):
    def __init__(self, id_usuario=None, usuario="", email="", contraseña=""):
        super().__init__(id_usuario=id_usuario, usuario=usuario, email=email, contraseña=contraseña, rol="admin")

    def modificar_rol(self, otro_usuario, nuevo_rol):
        if nuevo_rol.lower() not in Usuario.ROLES_VALIDOS:
            raise ValueError("Rol inválido")
        otro_usuario._rol = nuevo_rol.lower()
