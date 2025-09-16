import pytest
from datetime import datetime
from POO_SMARTHOME.estado_dispositivo import EstadoDispositivo

@pytest.fixture
def estado_dispositivo():
    fecha_inicial = datetime(2025, 1, 2, 3, 0, 0)
    return EstadoDispositivo(estado_actual="apagado", ultima_actualizacion=fecha_inicial)

def test_actualizar_estado(estado_dispositivo):
    fecha_inicial = estado_dispositivo.ultima_actualizacion
    estado_dispositivo.actualizar_estado("encendido")
    assert estado_dispositivo.estado_actual == "encendido"
    assert isinstance(estado_dispositivo.ultima_actualizacion, datetime)
    assert estado_dispositivo.ultima_actualizacion != fecha_inicial

def test_estado_property(estado_dispositivo):
    estado_dispositivo.estado_actual = "encendido"
    assert estado_dispositivo.estado_actual == "encendido"

def test_consultar_datos(estado_dispositivo):
    datos = estado_dispositivo.consultar_datos()
    assert datos["estado_actual"] == "apagado"
    assert isinstance(datos["ultima_actualizacion"], datetime)