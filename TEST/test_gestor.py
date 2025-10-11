import pytest
from POO_SMARTHOME.dispositivo import Dispositivo, GestorDispositivos

@pytest.fixture
def gestor():
    return GestorDispositivos()

def test_agregar_dispositivo(gestor):
    d = gestor.agregar_dispositivo("Lámpara", "LED")
    assert d.nombre == "Lámpara"
    assert d.tipo == "led"
    assert d.estado == "apagado"

def test_modificar_estado(gestor):
    gestor.agregar_dispositivo("Ventilador", "oscilante")
    assert gestor.modificar_estado_dispositivo("Ventilador", "encendido")
    assert gestor.buscar_por_nombre("Ventilador").estado == "encendido"

def test_eliminar_dispositivo(gestor):
    gestor.agregar_dispositivo("Calefactor", "eléctrico")
    assert gestor.eliminar_dispositivo("Calefactor")
    assert gestor.buscar_por_nombre("Calefactor") is None
