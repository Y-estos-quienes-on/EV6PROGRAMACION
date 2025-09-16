import unittest
from POO_SMARTHOME.dispositivo import GestorDispositivos, Dispositivo


class TestGestorDispositivos(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorDispositivos()

    def test_listar_estados_de_todos_los_dispositivos(self):
        self.gestor.agregar_dispositivo("A", "Tipo1", estado="Encendido")
        self.gestor.agregar_dispositivo("B", "Tipo2", estado="Apagado")
        self.gestor.agregar_dispositivo("C", "Tipo3", estado="Apagado")
        estados = [d.estado for d in self.gestor.listar_dispositivos()]
        self.assertEqual(estados, ["encendido", "apagado", "apagado"])
