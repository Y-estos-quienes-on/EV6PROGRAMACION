import hashlib #La usamos para codificar la contraseña

class Usuario:
    ROLES_VALIDOS = ["general", "admin", "invitado"]

    def __init__(self, usuario, email, contraseña, rol="general"):
        self._usuario = usuario
        self._email = email
        self.__contraseña = None
        self.cambiar_contraseña(contraseña)#Obligamos a que se valide la contraseña al momento de registro
        if rol not in self.ROLES_VALIDOS:
            raise ValueError(f"Rol invalido: {rol}")
        self._rol = rol

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        if not valor.strip():
            raise ValueError("El nombre de usuario no puede estar vacio")
        self._usuario = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ValueError("Email invalido")
        self._email = valor

    @property
    def rol(self):
        return self._rol

    def iniciar_sesion(self, usuario, contraseña):
        return self._usuario == usuario and self.__contraseña == hashlib.sha256(contraseña.encode()).hexdigest()

    def consultar_datos(self):
        return {"usuario": self._usuario, "email": self._email, "rol": self._rol}

    def cambiar_contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) < 5:
            raise ValueError("La contraseña es demasiado corta")
        self.__contraseña = hashlib.sha256(nueva_contraseña.encode()).hexdigest()


class Administrador(Usuario):
    def modificar_rol(self, usuario, nuevo_rol):
        if nuevo_rol not in Usuario.ROLES_VALIDOS:
            raise ValueError("Rol invalido")
        usuario._rol = nuevo_rol


class General(Usuario):
    pass
