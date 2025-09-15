from datetime import datetime

class ConsentimientoPrivacidad:
    def __init__(self, acepta_politicas, fecha, id_usuario, id_consentimiento):
        self._id_consentimiento = id_consentimiento
        self._acepta_politicas = acepta_politicas
        self._fecha = fecha
        self._id_usuario = id_usuario

    def dar_consentimiento(self):
        self._acepta_politicas = True
        self._fecha = datetime.now()

    def revocar_consentimiento(self):
        self._acepta_politicas = False
        self._fecha = datetime.now()

    def get_id_consentimiento(self):
        return self._id_consentimiento

    def set_id_consentimiento(self, id_consentimiento):
        self._id_consentimiento = id_consentimiento

    def get_acepta_politicas(self):
        return self._acepta_politicas

    def set_acepta_politicas(self, acepta_politicas):
        self._acepta_politicas = acepta_politicas

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, fecha):
        self._fecha = fecha

    def get_id_usuario(self):
        return self._id_usuario

    def set_id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
    def consultar_datos(self):
        return {
            "id_consentimiento": self._id_consentimiento,
            "acepta_politicas": self._acepta_politicas,
            "fecha": self._fecha,
            "id_usuario": self._id_usuario
        }