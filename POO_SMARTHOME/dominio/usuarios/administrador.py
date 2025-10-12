from dominio.usuarios.base import Usuario

class Administrador(Usuario):
    #Ejemplo de Metodo de administrador, revisar y agregar los correspondientes
    def modificar_rol(self, usuario, nuevo_rol):
        usuario.rol = nuevo_rol
