def interfazDispositivosUsuarioGeneral():

    while True: 
        print ("\n" + "="*50)
        print ("MIS DISPOSITIVOS")
        print ("="*50)
        print ("1. Ver mis dispositivos")
        print ("2. Volver atrás")
        print ("="*50)

        opcion = input("Seleccione una opción:").strip()

        if opcion == "1": 
            print("\n Dispositivos disponibles:")
            print("-Lámpara Cocina (luz)- Apagada")
            print("Cámara patio (cámara)- Encendida")

        elif opcion == "2":
            print ("Volviendo al menú principal")
            break

        else: 
            print ("Opción inválida")

def interfazDispositivosAdmin(): 

    while True: 
        print ("\n" + "="*50)
        print ("GESTIONAR DISPOSITIVOS")
        print ("\n" + "="*50)
        print ("1. Agregar dispositivo")
        print ("2. Ver todos los dispositivos")
        print ("3. Cambiar Estado")
        print ("4. Eliminar dispositivo")
        print ("5. Volver atrás")
        print ("\n" + "="*50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print ("\n AGREGAR DISPOSITIVO")
            nombre = input("Nombre: ").strip()
            tipo = input("Tipo (luz, cámara, etc.); ").strip()
            print (f"Dispositivo {nombre} agregado")

        elif opcion == "2":
            print("\n TODOS LOS DISPOSITIVOS:")
            print("Lámpara coocina (luz) -Apagada")
            print("Cámara patio (cámara) - Encendida")

        elif opcion == "3": 
            print("\n CAMBIAR ESTADO")
            nombre = input("Nombre del dispositivo: ").strip()
            nuevo_estado = input("Nuevo estado (encendido/apagado): ").strip()
            print(f"El estado de {nombre} cambió a {nuevo_estado}")

        elif opcion =="4": 
            print("\n ELIMINAR DISPOSITIVO")
            nombre = input("Nombre del dispositivo: ").strip()
            confirmacion = input (f"¿Desea eliminar {nombre} ? S / N: ").strip
            if confirmacion == "S": 
                print (f"Dispositivo {nombre} eliminado")
            elif confirmacion == "N":
                print("Cancelado. Volviendo al menú principal")
            else: 
                print("Opción inválida. Ingrese S o N ")

        elif opcion == "5": 
            print("Volviendo al menú principal")
            break
        
        else:
            print("Opción inválida")
