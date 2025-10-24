from datetime import datetime


class EstadoDispositivo:
    def __init__(self, id_estado=None, estado_actual="apagado"):
        self._id_estado = id_estado
        self._estado_actual = estado_actual
        self._ultima_actualizacion = datetime.now()

    @property
    def id_estado(self):
        return self._id_estado

    @id_estado.setter
    def id_estado(self, valor):
        self._id_estado = valor

    @property
    def estado_actual(self):
        return self._estado_actual

    @estado_actual.setter
    def estado_actual(self, valor):
        self._estado_actual = valor
        self._ultima_actualizacion = datetime.now()

    @property
    def ultima_actualizacion(self):
        return self._ultima_actualizacion