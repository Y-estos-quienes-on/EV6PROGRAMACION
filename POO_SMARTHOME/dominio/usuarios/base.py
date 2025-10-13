class Usuario:
    ROLES_VALIDOS = ["general", "admin"]

    def __init__(self, usuario, email, contraseña, rol="general"):
        self._usuario = None
        self._email = None
        self._contraseña = None
        self.usuario = usuario
        self.email = email
        self._contraseña = contraseña
        self._rol = rol if rol in self.ROLES_VALIDOS else "general"

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

    def iniciar_sesion(self, usuario, contraseña):
        return self._usuario == usuario and self._contraseña == contraseña

    def consultar_datos(self):
        return {
            "usuario": self._usuario,
            "email": self._email,
            "rol": self._rol
        }

    def cambiar_contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) < 4:
            raise ValueError("La contraseña es demasiado corta")
        self._contraseña = nueva_contraseña