from dao.estado_dispositivo_dao import EstadoDispositivoDAO
from dao.configuracion_dispositivo_dao import ConfiguracionDispositivoDAO
from dao.dispositivo_dao import DispositivoDAO
from dominio.dispositivos.dispositivo import Dispositivo
from dominio.dispositivos.estado_dispositivo import EstadoDispositivo
from dominio.dispositivos.configuracion_dispositivo import ConfiguracionDispositivo


class DispositivoService:
    def __init__(self):
        self.estado_dao = EstadoDispositivoDAO()
        self.config_dao = ConfiguracionDispositivoDAO()
        self.dispositivo_dao = DispositivoDAO()

    def registrar_dispositivo(self, nombre, tipo):

        estado = EstadoDispositivo(estado_actual="Apagado")
        id_estado = self.estado_dao.agregar_estado(estado)

        configuracion = ConfiguracionDispositivo(configuracion="{}")
        id_config = self.config_dao.agregar_configuracion(configuracion)

        dispositivo = Dispositivo(
            nombre=nombre,
            tipo_dispositivo=tipo,
            estado=id_estado,
            configuracion=id_config
        )

        id_dispositivo = self.dispositivo_dao.agregar_dispositivo(
            dispositivo,
            id_estado,
            id_config
        )

        return f"Dispositivo '{nombre}' (tipo: {tipo}) agregado con ID {id_dispositivo}."

    def listar_dispositivos(self):

        dispositivos = []
        filas = self.dispositivo_dao.obtener_todos_dispositivos()

        for fila in filas:
            id_disp, nombre, tipo, id_estado, id_config = fila

            estado = self.estado_dao.obtener_estado(id_estado)
            config = self.config_dao.obtener_configuracion(id_config)

            dispositivos.append({
                "id": id_disp,
                "nombre": nombre,
                "tipo": tipo,
                "estado": estado["estado_actual"] if estado else "Desconocido",
                "ultima_actualizacion": estado["ultima_actualizacion"] if estado else "-",
                "configuracion": config["configuracion"] if config else "Sin configuración",
                "timestamp": config["time_stamp"] if config else "-"
            })

        return dispositivos

    def actualizar_dispositivo(self, id_dispositivo: int, nombre=None, tipo=None, estado=None, configuracion=None):
        fila = self.dispositivo_dao.obtener_dispositivo(id_dispositivo)
        if not fila:
            return "No se encontró el dispositivo."

        id_estado = fila[3]
        id_config = fila[4]

        if nombre or tipo:
            self.dispositivo_dao.actualizar_dispositivo(id_dispositivo, nombre, tipo)

        if estado:
            nuevo_estado = EstadoDispositivo(estado_actual=estado)
            self.estado_dao.actualizar_estado(id_estado, nuevo_estado)

        if configuracion:
            self.config_dao.actualizar_configuracion(id_config, configuracion)

        return "Dispositivo actualizado correctamente."
    
    def eliminar_dispositivo(self, id_dispositivo):
        fila = self.dispositivo_dao.obtener_dispositivo(id_dispositivo)
        if not fila:
            return "No se encontró el dispositivo."

        id_estado = fila[3]
        id_config = fila[4]

   
        self.dispositivo_dao.eliminar_dispositivo(id_dispositivo)

        self.estado_dao.eliminar_estado(id_estado)
        self.config_dao.eliminar_configuracion(id_config)

        return f"Dispositivo con ID {id_dispositivo} eliminado correctamente."