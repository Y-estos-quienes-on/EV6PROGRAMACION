import unittest
from POO_SMARTHOME.usuario import Usuario

class TestUsuario(unittest.TestCase):

    def setUp(self):
                self.user = Usuario("Paola", "pao1@gmail.com", "1234", "general")
    
    def test_registrar(self):
        resultado = self.user.registrar()
        self.assertEqual(resultado, "Usuario Paola está registrado como general")
    def test_iniciar_sesion_correcta(self):
        self.assertTrue(self.user.iniciar_sesion("Paola", "1234"))

    def test_iniciar_sesion_incorrecta(self):
        self.assertFalse(self.user.iniciar_sesion("Paola", "0000"))

    def test_consultar_datos(self):
        datos = self.user.consultar_datos()
        self.assertEqual(datos["usuario"], "Paola")
        self.assertEqual(datos["email"], "pao1@gmail.com")
        self.assertEqual(datos["rol"], "general")

if __name__ == "__main__":
    unittest.main()