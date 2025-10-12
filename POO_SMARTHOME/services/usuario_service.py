#El service maneja la logica de negocio
from dominio.usuarios.base import Usuario
from dominio.usuarios.administrador import Administrador
from dao.usuario_dao import UsuarioDAO

class UsuarioService:
    def __init__(self):
        self.dao = UsuarioDAO()

    def registrar_usuario(self, nombre, email, contraseña, rol="general"):
        if rol == "admin":
            nuevo_usuario = Administrador(nombre, email, contraseña)
        else:
            nuevo_usuario = Usuario(nombre, email, contraseña, rol)
        self.dao.agregar_usuario(nuevo_usuario)
        return f"Usuario {nombre} registrado correctamente con rol {rol}."

    def iniciar_sesion(self, nombre: str, contraseña: str):
        usuario = self.dao.obtener_usuario(nombre)
        if usuario and usuario.iniciar_sesion(nombre, contraseña):
            return usuario
        return None

    def cambiar_rol(self, admin, nombre_usuario, nuevo_rol):
        usuario_objetivo = self.dao.obtener_usuario(nombre_usuario)
        if not usuario_objetivo:
            return "Usuario no encontrado."
        try:
            admin.modificar_rol(usuario_objetivo, nuevo_rol)
            self.dao.actualizar_usuario(usuario_objetivo)
            return f"Rol modificado a {nuevo_rol} correctamente."
        except ValueError as e:
            return f"Error: {e}"

    # Solo lectura para interfaces/admin
    def buscar_usuario(self, nombre: str):
        return self.dao.obtener_usuario(nombre)
