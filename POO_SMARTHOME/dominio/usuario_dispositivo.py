class UsuarioDispositivo:
    def __init__(self, id_usuario: int, id_dispositivo: int):
        self.id_usuario = id_usuario
        self.id_dispositivo = id_dispositivo

    def __repr__(self):
        return f"<UsuarioDispositivo usuario_id={self.id_usuario} dispositivo_id={self.id_dispositivo}>"
