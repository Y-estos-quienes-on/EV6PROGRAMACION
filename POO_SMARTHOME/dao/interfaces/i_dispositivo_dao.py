from abc import ABC, abstractmethod
from dominio.dispositivos.dispositivo import Dispositivo

class IDispositivoDAO(ABC):
    @abstractmethod
    def agregar_dispositivo(self, dispositivo: Dispositivo, id_estado: int, id_config: int) -> int:
        pass

    @abstractmethod
    def obtener_dispositivo(self, id_dispositivo: int):
        pass

    @abstractmethod
    def actualizar_dispositivo(self, id_dispositivo: int, nombre: str = None, tipo: str = None):
        pass

    @abstractmethod
    def eliminar_dispositivo(self, id_dispositivo: int):
        pass

    @abstractmethod
    def obtener_todos_dispositivos(self):
        pass
