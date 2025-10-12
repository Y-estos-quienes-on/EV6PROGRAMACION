from datetime import datetime

class ConfiguracionDispositivo:
    def __init__(self, estado: str, configuracion: str, time_stamp: datetime = None):
        self._estado = estado.lower()
        self._configuracion = configuracion
        self._time_stamp = time_stamp or datetime.now()

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado: str):
        self._estado = nuevo_estado.lower()
        self._time_stamp = datetime.now()

    @property
    def configuracion(self):
        return self._configuracion

    @configuracion.setter
    def configuracion(self, nueva_configuracion: str):
        self._configuracion = nueva_configuracion
        self._time_stamp = datetime.now()

    @property
    def time_stamp(self):
        return self._time_stamp

    def actualizar_configuracion(self, nuevo_estado: str, nueva_configuracion: str):
        self.estado = nuevo_estado
        self.configuracion = nueva_configuracion

    def consultar_datos(self):
        return {
            "estado": self.estado,
            "configuracion": self.configuracion,
            "time_stamp": self.time_stamp
        }