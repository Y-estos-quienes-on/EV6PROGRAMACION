from services.consentimiento_privacidad_service import ConsentimientoPrivacidadService

class Usuario:
    ROLES_VALIDOS = ["general", "admin"]

    def __init__(self, id_usuario=None, usuario="", email="", contraseña="", rol="general"):
        self._id_usuario = id_usuario
        self._usuario = None
        self._email = None
        self._contraseña = contraseña
        rol = rol.lower().strip()
        self._rol = rol if rol in self.ROLES_VALIDOS else "general"
        self.usuario = usuario
        self.email = email
        self.consent_service = ConsentimientoPrivacidadService()

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self._id_usuario = valor

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

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def contraseña(self, valor):
        if len(valor) < 4:
            raise ValueError("La contraseña es demasiado corta")
        self._contraseña = valor

    def iniciar_sesion(self, usuario, contraseña):
        return self._usuario == usuario and self._contraseña == contraseña

    def consultar_datos(self):
        consentimiento = {}
        if self._id_usuario:
            consentimiento = self.consent_service.obtener_consentimiento_por_id(self._id_usuario)
        acepto = "Aceptado" if consentimiento.get("acepta_politicas") else "No acepto"
        fecha = consentimiento.get("fecha", "-")

        return {
            "id_usuario": self._id_usuario,
            "usuario": self._usuario,
            "email": self._email,
            "rol": self._rol,
            "consentimiento_privacidad": acepto,
            "fecha_consentimiento": fecha
        }

    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña