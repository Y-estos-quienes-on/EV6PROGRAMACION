from services.usuario_service import UsuarioService
from services.dispositivo_service import DispositivoService
from presentation.interfaz_usuario import interfazAdmin as interfazUsuarioAdmin, interfazUsuarioGeneral
from presentation.interfaz_dispositivo import interfazDispositivosAdmin, interfazDispositivosUsuarioGeneral

def main():
    usuario_service = UsuarioService()
    dispositivo_service = DispositivoService()

    # Crear admin por defecto si no existe
    admin_existente = usuario_service.buscar_usuario("admin")
    if not admin_existente:
        print("Creando usuario admin por defecto...")
        usuario_service.registrar_usuario("admin", "admin@mail.com", "admin123", rol="admin")
        print("Usuario admin creado con usuario='admin' y contraseña='admin123'")

    # Menú de login
    while True:
        print("\n=== Sistema de Usuarios ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            nombre = input("Usuario: ").strip()
            email = input("Email: ").strip()
            contraseña = input("Contraseña: ").strip()
            rol = input("Rol (general/admin, opcional, default=general): ").strip().lower() or "general"
            print(usuario_service.registrar_usuario(nombre, email, contraseña, rol=rol))

        elif opcion == "2":
            nombre = input("Usuario: ").strip()
            contraseña = input("Contraseña: ").strip()
            usuario = usuario_service.iniciar_sesion(nombre, contraseña)

            if usuario:
                print(f"\nBienvenido {usuario.usuario}!")
                if usuario.rol == "admin":
                    # Menú admin principal
                    interfazUsuarioAdmin(usuario, usuario_service, dispositivo_service)
                else:
                    # Menú usuario general
                    interfazUsuarioGeneral(usuario, dispositivo_service)
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
