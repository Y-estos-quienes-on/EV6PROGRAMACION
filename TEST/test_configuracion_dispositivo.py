import pytest
from datetime import datetime
from POO_SMARTHOME.configuracion_dispositivo import ConfiguracionDispositivo

@pytest.fixture
def configuracion_dispositivo():
    fecha_inicial = datetime(2025, 1, 2, 3, 0, 0)
    return ConfiguracionDispositivo(
        estado="inactiva",
        configuracion="Modo Seguridad",
        time_stamp=fecha_inicial
    )

def test_actualizar_configuracion(configuracion_dispositivo):
    fecha_inicial = configuracion_dispositivo.time_stamp
    configuracion_dispositivo.actualizar_configuracion("activa", "Modo Noche")
    assert configuracion_dispositivo.estado == "activa"
    assert configuracion_dispositivo.configuracion == "Modo Seguridad"
    assert isinstance(configuracion_dispositivo.time_stamp, datetime)
    assert configuracion_dispositivo.time_stamp != fecha_inicial

def test_estado_property(configuracion_dispositivo):
    configuracion_dispositivo.estado = "activa"
    assert configuracion_dispositivo.estado == "activa"

def test_configuracion_property(configuracion_dispositivo):
    configuracion_dispositivo.configuracion = "Modo Seguridad"
    assert configuracion_dispositivo.configuracion == "Modo Seguridad"

def test_consultar_datos(configuracion_dispositivo):
    datos = configuracion_dispositivo.consultar_datos()
    assert datos["estado"] == "inactiva"
    assert datos["configuracion"] == "Modo Noche"
    assert isinstance(datos["time_stamp"], datetime)