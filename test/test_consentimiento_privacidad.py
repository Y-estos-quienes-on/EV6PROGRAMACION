import unittest
from datetime import datetime
from POO_SMARTHOME.consentimiento_privacidad import ConsentimientoPrivacidad

class TestConsentimientoPrivacidad(unittest.TestCase):

    def setUp(self):
        self.fecha_inicial = datetime(2025, 1, 1, 10, 0, 0)
        self.cp = ConsentimientoPrivacidad(
            acepta_politicas=False,
            fecha=self.fecha_inicial,
            id_usuario=1,
            id_consentimiento=10
        )

    def test_dar_consentimiento(self):
        self.cp.dar_consentimiento()
        self.assertTrue(self.cp.get_acepta_politicas())
        self.assertIsInstance(self.cp.get_fecha(), datetime)
        self.assertNotEqual(self.cp.get_fecha(), self.fecha_inicial)

    def test_revocar_consentimiento(self):
        self.cp.dar_consentimiento()
        self.cp.revocar_consentimiento()
        self.assertFalse(self.cp.get_acepta_politicas())
        self.assertIsInstance(self.cp.get_fecha(), datetime)
        self.assertNotEqual(self.cp.get_fecha(), self.fecha_inicial)

    def test_get_set_id_consentimiento(self):
        self.cp.set_id_consentimiento(2)
        self.assertEqual(self.cp.get_id_consentimiento(), 2)

    def test_get_set_acepta_politicas(self):
        self.cp.set_acepta_politicas(True)
        self.assertTrue(self.cp.get_acepta_politicas())

    def test_get_set_fecha(self):
        nueva_fecha = datetime(2025, 7, 1, 12, 15, 0)
        self.cp.set_fecha(nueva_fecha)
        self.assertEqual(self.cp.get_fecha(), nueva_fecha)

    def test_get_set_id_usuario(self):
        self.cp.set_id_usuario(3)
        self.assertEqual(self.cp.get_id_usuario(), 3)

    def test_consultar_datos(self):
        datos = self.cp.consultar_datos()
        self.assertEqual(datos["id_consentimiento"], 10)
        self.assertEqual(datos["acepta_politicas"], False)
        self.assertEqual(datos["fecha"], self.fecha_inicial)
        self.assertEqual(datos["id_usuario"], 1)

if __name__ == "__main__":
    unittest.main()