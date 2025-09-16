import pytest
from POO_SMARTHOME.usuario import Usuario

@pytest.fixture
def user():
    return Usuario("Paola", "pao1@gmail.com", 1234, "general")

def test_registrar(user):
    resultado = user.registrar()
    assert resultado == "Usuario Paola está registrado como general"

def test_iniciar_sesion_correcta(user):
    assert user.iniciar_sesion("Paola" , "1234") is True

def test_consultar_datos(user):
    datos = user.consultar_datos()
    assert datos["usuario"] == "Paola"
    assert datos["email"] == "pao1@gmail.com"
    assert datos["rol"] == "general"

def test_cambiar_contraseña(user):
    user.cambiar_contraseña("abcd")
    assert user.iniciar_sesion("Paola", "abcd") is True

def test_cambiar_contraseña_insegura(user):
    with pytest.raises(ValueError) as excinfo:
        user.cambiar_contraseña("123")  
    assert "La contraseña es insegura" in str(excinfo.value)

def test_email_invalido():
    with pytest.raises(ValueError) as excinfo:
        Usuario("Ana", "email_sin_arroba", "1234", "general")
    assert "Email inválido" in str(excinfo.value)

def test_rol_invalido():
    with pytest.raises(ValueError) as excinfo:
        Usuario("Ana", "ana@mail.com", "1234", "superuser")
    assert "Rol inválido" in str(excinfo.value)
