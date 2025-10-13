from dominio.usuarios.base import Usuario
from dominio.usuarios.administrador import Administrador
from dao.usuario_dao import UsuarioDAO

class UsuarioService:
    def __init__(self):
        self.dao = UsuarioDAO()

    def registrar_usuario(self, nombre: str, email: str, contraseña: str, rol: str = "general"):
        if not nombre.strip():
            return "El nombre de usuario no puede estar vacío."
        if "@" not in email or "." not in email:
            return "Email inválido."
        if len(contraseña) < 5:
            return "La contraseña es demasiado corta."

        rol = rol.lower().strip()
        if rol == "admin":
            nuevo_usuario = Administrador(usuario=nombre, email=email, contraseña=contraseña)
        else:
            nuevo_usuario = Usuario(usuario=nombre, email=email, contraseña=contraseña, rol=rol)

        self.dao.agregar_usuario(nuevo_usuario)
        return f"Usuario {nombre} registrado correctamente con rol {rol}."

    def iniciar_sesion(self, nombre: str, contraseña: str):
        usuario = self.dao.obtener_usuario(nombre)
        if not usuario:
            return None, "Usuario no encontrado."
        if not usuario.iniciar_sesion(nombre, contraseña):
            return None, "Contraseña incorrecta."
        return usuario, "Inicio de sesión exitoso."

    def cambiar_rol(self, admin, nombre_usuario: str, nuevo_rol: str):
        if not isinstance(admin, Administrador):
            return "Error: Solo un administrador puede cambiar roles."

        usuario_objetivo = self.dao.obtener_usuario(nombre_usuario)
        if not usuario_objetivo:
            return "Usuario no encontrado."

        try:
            admin.modificar_rol(usuario_objetivo, nuevo_rol.lower().strip())
            self.dao.actualizar_usuario(usuario_objetivo)
            return f"Rol modificado a {nuevo_rol} correctamente."
        except ValueError as e:
            return f"Error: {e}"

    def buscar_usuario(self, nombre: str):
        usuario = self.dao.obtener_usuario(nombre)
        if not usuario:
            return None, "Usuario no encontrado."
        return usuario, "Usuario encontrado."
