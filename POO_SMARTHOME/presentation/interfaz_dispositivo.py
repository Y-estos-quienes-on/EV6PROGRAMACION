from services.dispositivo_service import DispositivoService
from services.usuario_dispositivo_service import UsuarioDispositivoService

usuario_dispositivo_service = UsuarioDispositivoService()

def interfazDispositivosUsuarioGeneral(usuario, dispositivo_service: DispositivoService):
    while True:
        print("\n=== Mis Dispositivos ===")
        print("1. Ver mis dispositivos")
        print("2. Volver atrás")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            dispositivos, msg = usuario_dispositivo_service.obtener_dispositivos(usuario)
            if not dispositivos:
                print(msg)
            else:
                for d in dispositivos:
                    print(f"ID:{d.id_dispositivo} - {d.nombre} ({d.tipo_dispositivo}) - Estado: {d.estado.estado_actual} - Config: {d.configuracion.configuracion}")
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def interfazDispositivosAdmin(admin_usuario, dispositivo_service: DispositivoService):
    while True:
        print("\n=== Gestión de Dispositivos ===")
        print("1. Agregar dispositivo")
        print("2. Ver todos los dispositivos")
        print("3. Cambiar estado de un dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Volver atrás")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del dispositivo: ").strip()
            tipo = input("Tipo (luz, cámara, etc.): ").strip()
            msg = dispositivo_service.registrar_dispositivo(nombre, tipo)
            print(msg)

        elif opcion == "2":
            dispositivos = dispositivo_service.listar_dispositivos()
            if not dispositivos:
                print("No hay dispositivos registrados.")
            else:
                for d in dispositivos:
                    print(f"ID:{d['id']} - {d['nombre']} ({d['tipo']}) - Estado: {d['estado']} - Config: {d['configuracion']}")

        elif opcion == "3":
            id_disp = input("ID del dispositivo: ").strip()
            if not id_disp.isdigit():
                print("ID inválido.")
                continue
            id_disp = int(id_disp)
            nuevo_estado = input("Nuevo estado (encendido/apagado): ").strip()
            resultado = dispositivo_service.actualizar_dispositivo(id_disp, estado=nuevo_estado)
            print(resultado)

        elif opcion == "4":
            id_disp = input("ID del dispositivo a eliminar: ").strip()
            if not id_disp.isdigit():
                print("ID inválido.")
                continue
            id_disp = int(id_disp)
            resultado = dispositivo_service.eliminar_dispositivo(id_disp)
            print(resultado)

        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
