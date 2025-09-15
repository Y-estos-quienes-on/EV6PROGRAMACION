class UsuariosDispositivos:
    def __init__(self, id_usuario, dispositivos=None):
        self._id_usuario = id_usuario
        self._dispositivos = dispositivos if dispositivos is not None else []

    def agregar_dispositivo(self, dispositivo):
        if dispositivo not in self._dispositivos:
            self._dispositivos.append(dispositivo)

    def quitar_dispositivo(self, dispositivo):
        if dispositivo in self._dispositivos:
            self._dispositivos.remove(dispositivo)

    def consultar_datos(self):
        return {
            "id_usuario": self._id_usuario,
            "dispositivos": self._dispositivos
        }

    def get_id_usuario(self):
        return self._id_usuario

    def set_id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    def get_dispositivos(self):
        return self._dispositivos

    def set_dispositivos(self, dispositivos):
        self._dispositivos = dispositivos

    def mostrar_info(self):
        return f"Usuario {self._id_usuario} tiene los dispositivos: {', '.join(map(str, self._dispositivos))}"
