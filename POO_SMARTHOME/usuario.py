class Usuario: 
    def __init__(self, usuario, email, contraseña, rol): 
        self.usuario = usuario
        self._email = email
        self.__contraseña = contraseña
        self._rol = rol

    def registrar(self):
        return f"Usuario {self.usuario} está registrado como {self._rol}"

    def iniciar_sesion(self, usuario, contraseña):
        if self.usuario == usuario and self.__contraseña == contraseña:
            return True
        return False        

    def consultar_datos(self):
        return{
        "usuario": self.usuario, 
        "email": self._email,
        "rol": self._rol,

        }

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_rol(self):
        return self._rol

    def set_rol(self, rol):
        self._rol = rol