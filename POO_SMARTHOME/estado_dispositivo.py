from datetime import datetime

class EstadoDispositivo:
    def __init__(self, estado_actual: str, ultima_actualizacion: datetime = None):
        self._estado_actual = estado_actual.lower()
        self._ultima_actualizacion = ultima_actualizacion or datetime.now()

    @property
    def estado_actual(self):
        return self._estado_actual

    @estado_actual.setter
    def estado_actual(self, nuevo_estado: str):
        self._estado_actual = nuevo_estado.lower()
        self._ultima_actualizacion = datetime.now()

    @property
    def ultima_actualizacion(self):
        return self._ultima_actualizacion

    def actualizar_estado(self, nuevo_estado: str):
        self.estado_actual = nuevo_estado

    def consultar_datos(self):
        return {
            "estado_actual": self.estado_actual,
            "ultima_actualizacion": self.ultima_actualizacion
        }