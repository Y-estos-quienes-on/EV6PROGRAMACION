import unittest
from POO_SMARTHOME.dispositivo import Dispositivo, GestorDispositivos

class TestGestorDispositivos(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorDispositivos()

    def test_agregar_dispositivo(self):
        d = self.gestor.agregar_dispositivo("Lámpara", "LED")
        self.assertEqual(d.nombre, "Lámpara")
        self.assertEqual(d.tipo, "led")
        self.assertEqual(d.estado, "apagado")

    def test_modificar_estado(self):
        self.gestor.agregar_dispositivo("Ventilador", "oscilante")
        self.assertTrue(self.gestor.modificar_estado_dispositivo("Ventilador", "encendido"))
        self.assertEqual(self.gestor.buscar_por_nombre("Ventilador").estado, "encendido")

    def test_eliminar_dispositivo(self):
        self.gestor.agregar_dispositivo("Calefactor", "eléctrico")
        self.assertTrue(self.gestor.eliminar_dispositivo("Calefactor"))
        self.assertIsNone(self.gestor.buscar_por_nombre("Calefactor"))

if __name__ == "__main__":
    unittest.main()