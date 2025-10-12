from abc import ABC, abstractmethod
from dominio.usuarios.base import Usuario

class IUsuarioDAO(ABC):

    @abstractmethod
    def agregar_usuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def obtener_usuario(self, usuario_nombre: str) -> Usuario:
        pass

    @abstractmethod 
    def actualizar_usuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def eliminar_usuario(self, usuario: Usuario):
        pass
