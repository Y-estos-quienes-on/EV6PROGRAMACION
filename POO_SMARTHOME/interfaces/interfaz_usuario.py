from dominio.usuarios.base import Usuario, Administrador
from dao.interfaces.i_usuario_dao import IUsuarioDAO

def interfazUsuarioGeneral(usuario: Usuario):
    """
    Menú para usuarios estándar
    """
    while True:
        print("\n--- Menú Usuario ---")
        print("1. Consultar mis datos")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = usuario.consultar_datos()
            for clave, valor in datos.items():
                print(f"{clave}: {valor}")
        elif opcion == "2":
            print("Saliendo del menú de usuario...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def interfazAdmin(usuario: Administrador, dao: IUsuarioDAO):
    """
    Menú para administradores
    """
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Consultar usuario")
        print("2. Cambiar rol de usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de usuario a consultar: ")
            u = dao.obtenerUsuario(nombre)
            if u:
                datos = u.consultar_datos()
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
            else:
                print("Usuario no encontrado.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre de usuario a modificar: ")
            u = dao.obtenerUsuario(nombre)
            if u:
                nuevo_rol = input("Ingrese nuevo rol (general/admin/invitado): ").strip().lower()
                try:
                    usuario.modificar_rol(u, nuevo_rol)
                    dao.actualizarUsuario(u)
                    print(f"Rol modificado a {nuevo_rol} correctamente.")
                except ValueError as e:
                    print(e)
            else:
                print("Usuario no encontrado.")
        elif opcion == "3":
            print("Saliendo del menú de administrador...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
