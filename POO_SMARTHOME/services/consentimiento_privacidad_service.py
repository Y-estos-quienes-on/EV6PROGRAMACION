from dao.consentimiento_privacidad_dao import ConsentimientoPrivacidadDAO

class ConsentimientoPrivacidadService:
    def __init__(self):
        self.dao = ConsentimientoPrivacidadDAO()

    def registrar_consentimiento(self, id_usuario, acepta_politicas):
        self.dao.registrar_consentimiento(id_usuario, acepta_politicas)
        
    def obtener_consentimiento_por_id(self, id_usuario):
        return self.dao.obtener_consentimiento(id_usuario)

    def actualizar_consentimiento(self, id_usuario, acepta_politicas):
        self.dao.actualizar_consentimiento(id_usuario, acepta_politicas)
