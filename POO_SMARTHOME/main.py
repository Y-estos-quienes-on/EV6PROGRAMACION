from services.usuario_service import UsuarioService
from services.dispositivo_service import DispositivoService
from services.consentimiento_privacidad_service import ConsentimientoPrivacidadService
from presentation.interfaz_usuario import interfazAdmin as interfazUsuarioAdmin, interfazUsuarioGeneral

def main():
    usuario_service = UsuarioService()
    dispositivo_service = DispositivoService()
    consent_service = ConsentimientoPrivacidadService()

    # Crear admin por defecto si no existe
    admin, _ = usuario_service.buscar_usuario("admin")
    if not admin:
        print("Creando usuario admin por defecto")
        resultado = usuario_service.registrar_usuario("admin", "admin@gmail.com", "admin123", rol="admin")
        admin, _ = usuario_service.buscar_usuario("admin")
        consent_service.registrar(admin.id_usuario, True)
        print("Usuario admin creado con usuario='admin' y contraseña='admin123'")

    # Login y menú principal
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

            # Verificar si usuario existe
            usuario_existente, _ = usuario_service.buscar_usuario(nombre)
            if usuario_existente:
                print(f"El usuario '{nombre}' ya existe. No se puede registrar.")
                continue

            # Consentimiento
            acepta = input("¿Acepta la política de privacidad? (S/N): ").strip().upper()
            if acepta != "S":
                print("No se puede registrar el usuario sin aceptar la política de privacidad.")
                continue

            # Registrar usuario
            resultado = usuario_service.registrar_usuario(nombre, email, contraseña, rol=rol)
            print(resultado)
            usuario, _ = usuario_service.buscar_usuario(nombre)
            consent_service.registrar(usuario.id_usuario, True)
            print("Consentimiento registrado.")

        elif opcion == "2":
            nombre = input("Usuario: ").strip()
            contraseña = input("Contraseña: ").strip()
            usuario, msg = usuario_service.iniciar_sesion(nombre, contraseña)

            if usuario:
                print(f"\nBienvenido {usuario.usuario}!")
                if usuario.rol == "admin":
                    interfazUsuarioAdmin(usuario, usuario_service, dispositivo_service)
                else:
                    interfazUsuarioGeneral(usuario, dispositivo_service)
            else:
                print(msg)

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
