from services.usuario_service import UsuarioService
from services.dispositivo_service import DispositivoService
from services.consentimiento_privacidad_service import ConsentimientoPrivacidadService
from presentation.interfaz_usuario import interfazAdmin as interfazUsuarioAdmin, interfazUsuarioGeneral

def main():
    usuario_service = UsuarioService()
    dispositivo_service = DispositivoService()
    consent_service = ConsentimientoPrivacidadService()

    # Crear admin por defecto si no existe
    admin_existente = usuario_service.buscar_usuario("admin")
    if not admin_existente:
        print("Creando usuario admin por defecto...")
        usuario_service.registrar_usuario("admin", "admin@mail.com", "admin123", rol="admin")
        consent_service.registrar_consentimiento("admin", True)  # Guardar consentimiento
        print("Usuario admin creado con usuario='admin' y contraseña='admin123'")

    #Login
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

            #Checkin USUARIO
            if usuario_service.buscar_usuario(nombre):
                print(f"El usuario '{nombre}' ya existe. No se puede registrar.")
                continue

            #CONSENTIMIENTO
            acepta = input("¿Acepta la política de privacidad? (S/N): ").strip().upper()
            if acepta != "S":
                print("No se puede registrar el usuario sin aceptar la política de privacidad.")
                continue

            #Registrar
            resultado = usuario_service.registrar_usuario(nombre, email, contraseña, rol=rol)
            print(resultado)

            #RegistrarConsentimiento
            consent_service.registrar_consentimiento(nombre, True)
            print("Consentimiento registrado.")

        elif opcion == "2":
            nombre = input("Usuario: ").strip()
            contraseña = input("Contraseña: ").strip()
            usuario = usuario_service.iniciar_sesion(nombre, contraseña)

            if usuario:
                print(f"\nBienvenido {usuario.usuario}!")
                #MenuRoles
                if usuario.rol == "admin":
                    interfazUsuarioAdmin(usuario, usuario_service, dispositivo_service)
                else:
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
