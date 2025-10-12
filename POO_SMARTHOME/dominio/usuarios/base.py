import hashlib

class Usuario:
    ROLES_VALIDOS = ["general", "admin"]

    def __init__(self, usuario, email, contraseña, rol="general"):
        self._usuario = usuario
        self._email = email
        self.__contraseña = None
        self.cambiar_contraseña(contraseña)
        if rol not in self.ROLES_VALIDOS:
            raise ValueError(f"Rol inválido: {rol}")
        self._rol = rol

    #Propiedades
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

    #Metodos

    #Chequea  credenciales ingresadas con las del usuario
    def iniciar_sesion(self, usuario, contraseña):
        return (
            self._usuario == usuario and
            self.__contraseña == hashlib.sha256(contraseña.encode()).hexdigest()
        )
    #Devuelve datos del usuario
    def consultar_datos(self):
        return {
            "usuario": self._usuario,
            "email": self._email,
            "rol": self._rol
        }
    #Valida y encripta la nueva contraseña del usuario
    def cambiar_contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) < 5:
            raise ValueError("La contraseña es demasiado corta")
        self.__contraseña = hashlib.sha256(nueva_contraseña.encode()).hexdigest()

    #Devuelve la contraseña encriptada
    def get_hash_contraseña(self):
        return self.__contraseña
