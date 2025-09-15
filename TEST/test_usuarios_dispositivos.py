import unittest
from POO_SMARTHOME.usuarios_dispositivos import UsuariosDispositivos

class TestUsuariosDispositivos(unittest.TestCase):

    def setUp(self):
        self.usuarios_disp = UsuariosDispositivos(2, ["Lampara", "Cafetera"])

    def test_agregar_dispositivo(self):
        self.usuarios_disp.agregar_dispositivo("Alarma Patio")
        self.assertIn("Alarma Patio", self.usuarios_disp.get_dispositivos())
        self.usuarios_disp.agregar_dispositivo("Lampara")
        self.assertEqual(self.usuarios_disp.get_dispositivos().count("Lampara"), 1)

    def test_quitar_dispositivo(self):
        self.usuarios_disp.quitar_dispositivo("Lampara")
        self.assertNotIn("Lampara", self.usuarios_disp.get_dispositivos())
        self.usuarios_disp.quitar_dispositivo("Microondas")

    def test_consultar_datos(self):
        datos = self.usuarios_disp.consultar_datos()
        self.assertEqual(datos["id_usuario"], 2)
        self.assertEqual(datos["dispositivos"], ["Lampara", "Cafetera"])

    def test_get_set_id_usuario(self):
        self.usuarios_disp.set_id_usuario(2)
        self.assertEqual(self.usuarios_disp.get_id_usuario(), 2)

    def test_get_set_dispositivos(self):
        self.usuarios_disp.set_dispositivos(["Termotanque"])
        self.assertEqual(self.usuarios_disp.get_dispositivos(), ["Termotanque"])

if __name__ == "__main__":
    unittest.main()