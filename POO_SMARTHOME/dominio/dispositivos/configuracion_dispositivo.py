from datetime import datetime


class ConfiguracionDispositivo:
    def __init__(self, id_configuracion=None, estado=1, configuracion="default"):
        self._id_configuracion = id_configuracion
        self._estado = estado  # 1 = activo, 0 = inactivo
        self._configuracion = configuracion
        self._time_stamp = datetime.now()

    @property
    def id_configuracion(self):
        return self._id_configuracion

    @id_configuracion.setter
    def id_configuracion(self, valor):
        self._id_configuracion = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

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