from abc import ABC, abstractmethod

class IConsentimientoPrivacidadDAO(ABC):
    @abstractmethod
    def registrar_consentimiento(self, usuario: str, aceptado: bool):
        pass

    @abstractmethod
    def verificar_consentimiento(self, usuario: str) -> bool:
        pass

    @abstractmethod
    def actualizar_consentimiento(self, usuario: str, aceptado: bool):
        pass

    @abstractmethod
    def obtener_consentimiento(self, usuario: str) -> bool:
        pass
