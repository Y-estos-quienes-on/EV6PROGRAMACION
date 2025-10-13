from abc import ABC, abstractmethod

class IUsuarioDispositivoDAO(ABC):
    @abstractmethod
    def asignar_dispositivo(self, id_usuario: int, id_dispositivo: int):
        pass

    @abstractmethod
    def quitar_dispositivo(self, id_usuario: int, id_dispositivo: int):
        pass

    @abstractmethod
    def obtener_dispositivos_de_usuario(self, id_usuario: int):
        pass

    @abstractmethod
    def obtener_usuarios_de_dispositivo(self, id_dispositivo: int):
        pass
