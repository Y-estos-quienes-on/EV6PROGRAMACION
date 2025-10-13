from abc import ABC, abstractmethod
from dominio.dispositivos.configuracion_dispositivo import ConfiguracionDispositivo

class IConfiguracionDispositivoDAO(ABC):
    @abstractmethod
    def agregar_configuracion(self, config: ConfiguracionDispositivo) -> int:
        pass

    @abstractmethod
    def obtener_configuracion(self, id_config: int) -> ConfiguracionDispositivo:
        pass

    @abstractmethod
    def actualizar_configuracion(self, id_config: int, nueva_config: str):
        pass

    @abstractmethod
    def eliminar_configuracion(self, id_config: int):
        pass
