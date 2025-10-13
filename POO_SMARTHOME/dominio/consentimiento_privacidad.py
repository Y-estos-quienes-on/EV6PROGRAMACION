from datetime import datetime

class ConsentimientoPrivacidad:
    def __init__(self, usuario, aceptado=False):
        self._usuario = usuario
        self._aceptado = aceptado
        self._fecha = datetime.now()

    @property
    def usuario(self):
        return self._usuario

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
