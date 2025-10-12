class UsuariosDispositivos:
    def __init__(self, id_usuario, dispositivos=None):
        self.id_usuario = id_usuario
        self._dispositivos = dispositivos if dispositivos is not None else []

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("El id de usuario no puede estar vacío")
        self._id_usuario = valor

    @property
    def dispositivos(self):
        return self._dispositivos

    @dispositivos.setter
    def dispositivos(self, lista):
        if not isinstance(lista, list):
            raise ValueError("Los dispositivos deben estar en una lista")
        self._dispositivos = lista

    def agregar_dispositivo(self, dispositivo):
        if dispositivo not in self._dispositivos:
            self._dispositivos.append(dispositivo)

    def quitar_dispositivo(self, dispositivo):
        if dispositivo in self._dispositivos:
            self._dispositivos.remove(dispositivo)

    def consultar_datos(self):
        return {
            "id_usuario": self.id_usuario,
            "dispositivos": self.dispositivos
        }

    def mostrar_info(self):
        if not self._dispositivos:
            return f"Usuario {self.id_usuario} no tiene dispositivos registrados"
        return f"Usuario {self.id_usuario} tiene los dispositivos: {', '.join(map(str, self._dispositivos))}"
