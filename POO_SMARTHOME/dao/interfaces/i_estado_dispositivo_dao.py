from abc import ABC, abstractmethod
from dominio.dispositivos.estado_dispositivo import EstadoDispositivo

class IEstadoDispositivoDAO(ABC):
    @abstractmethod
    def agregar_estado(self, estado: EstadoDispositivo) -> int:
        pass

    @abstractmethod
    def obtener_estado(self, id_estado: int) -> EstadoDispositivo:
        pass

    @abstractmethod
    def actualizar_estado(self, id_estado: int, nuevo_estado: str):
        pass

    @abstractmethod
    def eliminar_estado(self, id_estado: int):
        pass
