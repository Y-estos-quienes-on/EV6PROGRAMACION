from dominio.usuarios.base import Usuario
from dominio.usuarios.administrador import Administrador
from services.usuario_service import UsuarioService
from presentation.interfaz_dispositivo import interfazDispositivosUsuarioGeneral, interfazDispositivosAdmin

def interfazUsuarioGeneral(usuario: Usuario, dispositivo_service):
    while True:
        print("\n--- Menú Usuario ---")
        print("1. Consultar mis datos")
        print("2. Mis dispositivos")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            datos = usuario.consultar_datos()
            for clave, valor in datos.items():
                print(f"{clave}: {valor}")
        elif opcion == "2":
            interfazDispositivosUsuarioGeneral(usuario, dispositivo_service)
        elif opcion == "3":
            print("Saliendo del menú de usuario...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def interfazAdmin(usuario_admin: Administrador, service: UsuarioService, dispositivo_service):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Consultar usuario")
        print("2. Cambiar rol de usuario")
        print("3. Gestionar dispositivos")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre de usuario a consultar: ").strip()
            u, msg = service.buscar_usuario(nombre)
            if u:
                datos = u.consultar_datos()
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
            else:
                print(msg)
        elif opcion == "2":
            nombre = input("Ingrese el nombre de usuario a modificar: ").strip()
            u, msg = service.buscar_usuario(nombre)
            if u:
                nuevo_rol = input("Ingrese nuevo rol (general/admin): ").strip().lower()
                print(service.cambiar_rol(usuario_admin, nombre, nuevo_rol))
            else:
                print(msg)
        elif opcion == "3":
            interfazDispositivosAdmin(usuario_admin, dispositivo_service)
        elif opcion == "4":
            print("Saliendo del menú de administrador...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
