from dominio.dispositivos.estado_dispositivo import EstadoDispositivo
from dominio.dispositivos.configuracion_dispositivo import ConfiguracionDispositivo

class Dispositivo:
    def __init__(self, nombre, tipo_dispositivo, estado=None, configuracion=None):
        self._nombre = nombre
        self._tipo_dispositivo = tipo_dispositivo
        self._estado = estado if estado else EstadoDispositivo()
        self._configuracion = configuracion if configuracion else ConfiguracionDispositivo()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def tipo_dispositivo(self):
        return self._tipo_dispositivo

    @tipo_dispositivo.setter
    def tipo_dispositivo(self, valor):
        self._tipo_dispositivo = valor

    @property
    def estado(self):
        return self._estado

    @property
    def configuracion(self):
        return self._configuracion
