from dao.usuario_dispositivo_dao import UsuarioDispositivoDAO
from dominio.usuarios.base import Usuario
from dominio.dispositivos.dispositivo import Dispositivo

class UsuarioDispositivoService:
    def __init__(self):
        self.dao = UsuarioDispositivoDAO()

    def asignar_dispositivo(self, usuario: Usuario, dispositivo: Dispositivo):
        if usuario.id_usuario is None or dispositivo.id_dispositivo is None:
            return "Error: Usuario o dispositivo sin ID."
        self.dao.asignar_dispositivo(usuario.id_usuario, dispositivo.id_dispositivo)
        return f"Dispositivo '{dispositivo.nombre}' asignado a usuario '{usuario.usuario}'."

    def quitar_dispositivo(self, usuario: Usuario, dispositivo: Dispositivo):
        if usuario.id_usuario is None or dispositivo.id_dispositivo is None:
            return "Error: Usuario o dispositivo sin ID."
        self.dao.quitar_dispositivo(usuario.id_usuario, dispositivo.id_dispositivo)
        return f"Dispositivo '{dispositivo.nombre}' desvinculado de usuario '{usuario.usuario}'."

    def obtener_dispositivos(self, usuario: Usuario):
        dispositivos = self.dao.obtener_dispositivos_de_usuario(usuario.id_usuario)
        return dispositivos, f"{len(dispositivos)} dispositivo(s) encontrados para '{usuario.usuario}'."

    def obtener_usuarios(self, dispositivo: Dispositivo):
        usuarios = self.dao.obtener_usuarios_de_dispositivo(dispositivo.id_dispositivo)
        return usuarios, f"{len(usuarios)} usuario(s) encontrados para '{dispositivo.nombre}'."
