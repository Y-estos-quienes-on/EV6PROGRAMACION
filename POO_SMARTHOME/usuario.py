class Usuario: 
    ROLES_VALIDOS = ["general", "admin", "invitado"]
    
    def __init__(self, usuario, email, contraseña, rol):
        self.usuario = usuario
        self._email = email
        self.__contraseña = None
        self.cambiar_contraseña(contraseña)
        self._rol = rol

    @property
    def usuario(self):
        return self.usuario

    @usuario.setter 
    def usuario(self, valor): 
        if not valor or valor.strip() == "":
            raise ValueError("El nombre de usuario no puede estar vacío")
        self.usuario = valor

    @property
    def email(self):
        return self.email
    
    @email.setter 
    def email(self,valor):
        if "@" not in valor or "."not in valor:
            raise ValueError("Email inválido")
        self.email = valor

    @property
    def rol(self):
        return self.rol
    
    def registrar(self):
        return f"Usuario {self.usuario} está registrado como {self.rol}"
    
    def iniciar_sesion(self, usuario, contraseña):
        return self.usuario == usuario and self.__contraseña == contraseña
    
    def consultar_datos(self):
        return {
            "usuario": self.usuario,
            "email": self.email,
            "rol": self.rol 
        }
    def cambiar_contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) <4:
            raise ValueError("La contraseña es demasiado corta")
        self.__contraseña = nueva_contraseña
