class Usuario:
    ROLES_VALIDOS = ["general", "admin", "invitado"]

    def __init__(self, usuario, email, contraseña, rol):
        self._usuario = usuario
        self._email = email
        self.__contraseña = None
        self.cambiar_contraseña(contraseña)
        self._rol = rol

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        if not valor.strip():
            raise ValueError("El nombre de usuario no puede estar vacío")
        self._usuario = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ValueError("Email inválido")
        self._email = valor

    @property
    def rol(self):
        return self._rol

    def registrar(self):
        return f"Usuario {self._usuario} está registrado como {self._rol}"

    def iniciar_sesion(self, usuario, contraseña):
        return self._usuario == usuario and self.__contraseña == contraseña

    def consultar_datos(self):
        return {"usuario": self._usuario, "email": self._email, "rol": self._rol}

    def cambiar_contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) < 4:
            raise ValueError("La contraseña es demasiado corta")
        self.__contraseña = nueva_contraseña


class Administrador(Usuario):
    def modificar_rol(self, usuario, nuevo_rol):
        if nuevo_rol not in Usuario.ROLES_VALIDOS:
            raise ValueError("Rol inválido")
        usuario._rol = nuevo_rol


class General(Usuario):
    pass
