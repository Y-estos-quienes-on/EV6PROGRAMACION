from services.usuario_service import UsuarioService
from interfaces.interfaz_usuario import interfazAdmin, interfazUsuarioGeneral

def main():
    service = UsuarioService()

    #Crear admin por defecto si no existe
    admin_inicial = service.iniciar_sesion("admin", "admin123")
    if not admin_inicial:
        print("Creando usuario admin por defecto...")
        service.registrar_usuario("admin", "admin@mail.com", "admin123", rol="admin")
        print("Usuario admin creado con usuario='admin' y contraseña='admin123'")

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
            rol = input("Rol (general/admin, opcional, default=general): ").strip().lower() or "general"
            print(service.registrar_usuario(nombre, email, contraseña, rol=rol))

        elif opcion == "2":
            nombre = input("Usuario: ").strip()
            contraseña = input("Contraseña: ").strip()
            usuario = service.iniciar_sesion(nombre, contraseña)

            if usuario:
                print(f"\nBienvenido {usuario.usuario}!")
                if usuario.rol == "admin":
                    interfazAdmin(usuario, service)
                else:
                    interfazUsuarioGeneral(usuario)
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción invalida. Intente nuevamente.")

if __name__ == "__main__":
    main()
