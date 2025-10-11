import pytest
from datetime import datetime
import time
from POO_SMARTHOME.consentimiento_privacidad import ConsentimientoPrivacidad

@pytest.fixture
def consentimiento():
    fecha_inicial = datetime(2025, 1, 1, 10, 0, 0)
    return ConsentimientoPrivacidad(
        acepta_politicas=False,
        fecha=fecha_inicial,
        id_usuario=1,
        id_consentimiento=10
    )

def test_dar_consentimiento(consentimiento):
    fecha_inicial = consentimiento.fecha
    consentimiento.dar_consentimiento()
    assert consentimiento.acepta_politicas is True
    assert isinstance(consentimiento.fecha, datetime)
    assert consentimiento.fecha != fecha_inicial

def test_revocar_consentimiento(consentimiento):
    consentimiento.dar_consentimiento()
    fecha_aceptado = consentimiento.fecha
    time.sleep(0.001) #me tira error por 1 microsegundo :)
    consentimiento.revocar_consentimiento()
    assert consentimiento.acepta_politicas is False
    assert isinstance(consentimiento.fecha, datetime)
    assert consentimiento.fecha != fecha_aceptado

def test_id_consentimiento_property(consentimiento):
    consentimiento.id_consentimiento = 2
    assert consentimiento.id_consentimiento == 2

def test_acepta_politicas_property(consentimiento):
    consentimiento.acepta_politicas = True
    assert consentimiento.acepta_politicas is True

def test_fecha_property(consentimiento):
    nueva_fecha = datetime(2025, 7, 1, 12, 15, 0)
    consentimiento.fecha = nueva_fecha
    assert consentimiento.fecha == nueva_fecha

def test_id_usuario_property(consentimiento):
    consentimiento.id_usuario = 3
    assert consentimiento.id_usuario == 3

def test_consultar_datos(consentimiento):
    datos = consentimiento.consultar_datos()
    assert datos["id_consentimiento"] == 10
    assert datos["acepta_politicas"] is False
    assert isinstance(datos["fecha"], datetime)
    assert datos["id_usuario"] == 1
