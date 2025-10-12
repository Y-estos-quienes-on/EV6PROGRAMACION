from dominio.usuarios.base import Usuario
from dominio.usuarios.administrador import Administrador
from services.usuario_service import UsuarioService


def interfazUsuarioGeneral(usuario: Usuario):
    #MenuGeneral
    while True:
        print("\n--- Menu Usuario ---")
        print("1. Consultar mis datos")
        print("2. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            datos = usuario.consultar_datos()
            for clave, valor in datos.items():
                print(f"{clave}: {valor}")
        elif opcion == "2":
            print("Saliendo del menu de usuario...")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")


def interfazAdmin(usuario_admin: Administrador, service: UsuarioService):
    #MenuAdmin 
    while True:
        print("\n--- Menu Administrador ---")
        print("1. Consultar usuario")
        print("2. Cambiar rol de usuario")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de usuario a consultar: ")
            u = service.buscar_usuario(nombre)
            if u:
                datos = u.consultar_datos()
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
            else:
                print("Usuario no encontrado.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre de usuario a modificar: ")
            u = service.buscar_usuario(nombre) 
            if u:
                nuevo_rol = input("Ingrese nuevo rol (general/admin): ").strip().lower()
                print(service.cambiar_rol(usuario_admin, nombre, nuevo_rol))
            else:
                print("Usuario no encontrado.")

        elif opcion == "3":
            print("Saliendo del menu de administrador...")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
