from abc import ABC, abstractmethod
from dominio.usuarios.base import Usuario

class IUsuarioDAO(ABC):

    @abstractmethod
    def agregarUsuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def obtenerUsuario(self, usuario_nombre: str) -> Usuario:
        pass

    @abstractmethod 
    def actualizarUsuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def eliminarUsuario(self, usuario: Usuario):
        pass
