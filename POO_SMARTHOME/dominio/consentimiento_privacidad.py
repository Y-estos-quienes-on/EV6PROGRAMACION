from datetime import datetime


class ConsentimientoPrivacidad:
    def __init__(self, id_consentimiento=None, id_usuario=None, aceptado=False, fecha=None):
        self._id_consentimiento = id_consentimiento
        self._id_usuario = id_usuario
        self._aceptado = aceptado
        self._fecha = fecha if fecha else datetime.now()

    @property
    def id_consentimiento(self):
        return self._id_consentimiento

    @id_consentimiento.setter
    def id_consentimiento(self, valor):
        self._id_consentimiento = valor

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self._id_usuario = valor

    @property
    def aceptado(self):
        return self._aceptado

    @aceptado.setter
    def aceptado(self, valor: bool):
        self._aceptado = valor
        self._fecha = datetime.now()

    @property
    def fecha(self):
        return self._fecha

    def formato_mysql(self):
        """Formato de MySQL"""
        return self._fecha.strftime('%Y-%m-%d %H:%M:%S')