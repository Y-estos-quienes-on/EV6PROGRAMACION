from services.consentimiento_privacidad_service import ConsentimientoPrivacidadService

def interfazConsentimiento(usuario, service: ConsentimientoPrivacidadService):
    print("\n--- Consentimiento de Privacidad ---")
    c = service.obtener_consentimiento(usuario)
    if c and c.aceptado:
        print("Ya aceptaste el consentimiento de privacidad.")
        return True

    opcion = input("¿Acepta el consentimiento de privacidad? (S/N): ").strip().upper()
    if opcion == "S":
        service.registrar_consentimiento(usuario, True)
        print("Consentimiento aceptado.")
        return True
    else:
        service.registrar_consentimiento(usuario, False)
        print("Consentimiento rechazado. No podrás usar algunas funciones.")
        return False
