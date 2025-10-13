from abc import ABC, abstractmethod

class IConsentimientoPrivacidadDAO(ABC):

    @abstractmethod
    def registrar_consentimiento(self, usuario: str, aceptado: bool):
        pass

    @abstractmethod
    def verificar_consentimiento(self, usuario: str) -> bool:
        """Devuelve True si el usuario ya aceptó, False si no."""
        pass
