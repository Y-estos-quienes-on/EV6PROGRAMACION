from datetime import datetime

class ConfiguracionDispositivo:
    def __init__(self, configuracion="default"):
        self._configuracion = configuracion
        self._time_stamp = datetime.now()

    @property
    def configuracion(self):
        return self._configuracion

    @configuracion.setter
    def configuracion(self, valor):
        self._configuracion = valor
        self._time_stamp = datetime.now()

    @property
    def time_stamp(self):
        return self._time_stamp
