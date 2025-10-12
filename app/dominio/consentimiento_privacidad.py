from datetime import datetime

class ConsentimientoPrivacidad:
    def __init__(self, acepta_politicas, fecha, id_usuario, id_consentimiento):
        self.id_consentimiento = id_consentimiento
        self.acepta_politicas = acepta_politicas
        self.fecha = fecha
        self.id_usuario = id_usuario

    @property
    def id_consentimiento(self):
        return self._id_consentimiento

    @id_consentimiento.setter
    def id_consentimiento(self, value):
        if not value or str(value).strip() == "":
            raise ValueError("El id de consentimiento no puede estar vacío")
        self._id_consentimiento = value

    @property
    def acepta_politicas(self):
        return self._acepta_politicas

    @acepta_politicas.setter
    def acepta_politicas(self, value):
        if not isinstance(value, bool):
            raise ValueError("acepta_politicas debe ser True o False")
        self._acepta_politicas = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        if not isinstance(value, datetime):
            raise ValueError("fecha debe ser un objeto datetime")
        self._fecha = value

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, value):
        if not value or str(value).strip() == "":
            raise ValueError("El id de usuario no puede estar vacío")
        self._id_usuario = value

    def dar_consentimiento(self):
        self._acepta_politicas = True
        self._fecha = datetime.now()

    def revocar_consentimiento(self):
        self._acepta_politicas = False
        self._fecha = datetime.now()

    def consultar_datos(self):
        return {
            "id_consentimiento": self.id_consentimiento,
            "acepta_politicas": self.acepta_politicas,
            "fecha": self.fecha,
            "id_usuario": self.id_usuario
        }
