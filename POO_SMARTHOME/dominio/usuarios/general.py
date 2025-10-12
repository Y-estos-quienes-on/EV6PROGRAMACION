from dominio.usuarios.base import Usuario

class General(Usuario):
    def __init__(self, usuario, email, contraseña):
        super().__init__(usuario, email, contraseña, rol="general")
