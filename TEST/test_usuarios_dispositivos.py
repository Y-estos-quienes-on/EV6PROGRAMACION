import pytest
from POO_SMARTHOME.usuarios_dispositivos import UsuariosDispositivos

@pytest.fixture
def usuarios_disp():
    return UsuariosDispositivos(2, ["Lampara", "Cafetera"])

def test_agregar_dispositivo(usuarios_disp):
    usuarios_disp.agregar_dispositivo("Alarma Patio")
    assert "Alarma Patio" in usuarios_disp.dispositivos
    usuarios_disp.agregar_dispositivo("Lampara")
    assert usuarios_disp.dispositivos.count("Lampara") == 1

def test_quitar_dispositivo(usuarios_disp):
    usuarios_disp.quitar_dispositivo("Lampara")
    assert "Lampara" not in usuarios_disp.dispositivos
    usuarios_disp.quitar_dispositivo("Microondas")

def test_consultar_datos(usuarios_disp):
    datos = usuarios_disp.consultar_datos()
    assert datos["id_usuario"] == 2
    assert datos["dispositivos"] == ["Lampara", "Cafetera"]

def test_id_usuario_property(usuarios_disp):
    usuarios_disp.id_usuario = 5
    assert usuarios_disp.id_usuario == 5

def test_dispositivos_property(usuarios_disp):
    usuarios_disp.dispositivos = ["Termotanque"]
    assert usuarios_disp.dispositivos == ["Termotanque"]
