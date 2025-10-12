from dominio.usuarios.base import Usuario
from dao.usuario_dao import UsuarioDAO
from interfaces.interfaz_usuario import interfazUsuarioGeneral, interfazAdmin

def main():
    dao = UsuarioDAO()

    while True:
        print("\n=== Sistema de Usuarios ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Usuario: ").strip()
            email = input("Email: ").strip()
            contraseña = input("Contraseña: ").strip()
            try:
                u = Usuario(nombre, email, contraseña)
                dao.agregarUsuario(u)
                print(f"Usuario {nombre} registrado correctamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            nombre = input("Usuario: ").strip()
            contraseña = input("Contraseña: ").strip()
            u = dao.obtenerUsuario(nombre)
            if u and u.iniciar_sesion(nombre, contraseña):
                print(f"\n¡Bienvenido {u.usuario}!")
                if u.rol == "admin":
                    interfazAdmin(u, dao)
                else:
                    interfazUsuarioGeneral(u)
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
