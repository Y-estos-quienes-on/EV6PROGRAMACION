from dao.consentimiento_privacidad_dao import ConsentimientoPrivacidadDAO
from dominio.consentimiento_privacidad import ConsentimientoPrivacidad

class ConsentimientoPrivacidadService:
    def __init__(self):
        self.dao = ConsentimientoPrivacidadDAO()

    def registrar_consentimiento(self, usuario, aceptado: bool):
        consentimiento = ConsentimientoPrivacidad(usuario, aceptado)
        self.dao.registrar_consentimiento(usuario, aceptado)
        return f"Consentimiento para {usuario} registrado."

    def obtener_consentimiento(self, usuario):
        return self.dao.verificar_consentimiento(usuario)

    def cambiar_consentimiento(self, usuario, aceptado: bool):
        self.dao.actualizar_consentimiento(usuario, aceptado)
        return f"Consentimiento para {usuario} actualizado a {'aceptado' if aceptado else 'rechazado'}."
